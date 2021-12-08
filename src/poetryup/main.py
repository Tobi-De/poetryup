#!/usr/bin/env python

import logging
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import List

import tomlkit
import typer
from tomlkit.items import String
from tomlkit.toml_document import TOMLDocument

from poetryup import utils

app = typer.Typer(add_completion=False)


@dataclass
class Dependency:
    name: str
    version: str


def _setup_logging() -> None:
    """Setup and configure logging"""

    logging.basicConfig(level=logging.INFO)


def _run_poetry_update() -> None:
    """Run poetry update command"""

    subprocess.run(["poetry", "update"])


def _run_poetry_add(package: str) -> None:
    """Run poetry add command

    Args:
        package (str): The package to add
    """

    subprocess.run(["poetry", "add", package])


def _run_poetry_show() -> str:
    """Run poetry show command

    Returns:
        str: The output from the poetry show command
    """

    return subprocess.run(
        ["poetry", "show", "--tree"], capture_output=True
    ).stdout.decode()


def _list_dependencies() -> List[Dependency]:
    """List all top-level dependencies

    Returns:
        List[Dependency]: A list of dependencies
    """

    output = _run_poetry_show()

    pattern = re.compile("^[a-zA-Z-]+")
    dependencies: List[Dependency] = []
    for line in output.split("\n"):
        if pattern.match(line) is not None:
            name, version, *_ = line.split()
            dependency = Dependency(name=name, version=version)
            dependencies.append(dependency)

    return dependencies


def _bump_versions_in_pyproject(
    dependencies: List[Dependency], pyproject: TOMLDocument
) -> TOMLDocument:
    """Bump versions in pyproject

    Args:
        dependencies (List[Dependency]): A list of dependencies
        pyproject (TOMLDocument): The pyproject file parsed as a TOMLDocument

    Returns:
        TOMLDocument: The updated pyproject
    """

    logging.info(f"Found {len(dependencies)} dependencies in pyproject.toml")

    for dependency in dependencies:
        value = utils.lookup_tomlkit_table(
            table=pyproject["tool"]["poetry"], key=dependency.name
        )

        if type(value) is not String:
            logging.info(
                f"Bumping skipped for dependency named: {dependency.name}"
            )
            continue  # skip if dependency is complex or if not found

        if value.startswith(("^", "~")):
            new_version = value[0] + dependency.version
            utils.update_tomlkit_table(
                table=pyproject["tool"]["poetry"],
                key=dependency.name,
                new_value=new_version,
            )

    return pyproject


def poetryup(pyproject_str: str, latest: bool = False) -> str:
    """Update dependencies and bump their version

    Args:
        pyproject_str (str): The pyproject file parsed as a string
        latest (bool): Indicates whether to update dependencies to their latest
                       available version, defaults to false

    Returns:
        str: The updated pyproject string
    """

    if latest:
        logging.info("Updating dependencies to their latest available version")
        dependencies = _list_dependencies()
        for dependency in dependencies:
            _run_poetry_add(f"{dependency.name}@latest")
    else:
        _run_poetry_update()

    dependencies = _list_dependencies()
    pyproject = tomlkit.loads(pyproject_str)
    updated_pyproject = _bump_versions_in_pyproject(dependencies, pyproject)

    return tomlkit.dumps(updated_pyproject)


@app.command()
def main(
    latest: bool = typer.Option(
        default=False,
        help="Whether to update dependencies to their latest version.",
    ),
):
    """Update dependencies and bump their version in pyproject.toml file"""

    _setup_logging()

    # read pyproject.toml file
    try:
        pyproject_str = Path("pyproject.toml").read_text()
    except FileNotFoundError:
        raise Exception(
            "poetryup couldn't find a pyproject.toml file in current directory"
        )

    updated_pyproject_str = poetryup(pyproject_str, latest)
    Path("pyproject.toml").write_text(updated_pyproject_str)


if __name__ == "__main__":
    app()
