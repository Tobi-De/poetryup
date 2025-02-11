import os
from pathlib import Path

from pytest_mock import MockerFixture

from poetryup.pyproject import Pyproject


def test_update_dependencies(
    mock_poetry_commands,
) -> None:
    pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/input_pyproject/pyproject.toml",
        )
    ).read_text()
    expected_pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/expected_pyproject/pyproject.toml",
        )
    ).read_text()

    pyproject = Pyproject(pyproject_str)
    pyproject.update_dependencies()
    assert pyproject.dumps() == expected_pyproject_str
    assert (
        pyproject.pyproject["tool"]["poetry"]["dependencies"]["poetryup"]
        == "^0.2.0"
    )


def test_update_dependencies_latest(
    mock_poetry_commands,
) -> None:
    pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/input_pyproject/pyproject.toml",
        )
    ).read_text()
    expected_pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/expected_pyproject/pyproject.toml",
        )
    ).read_text()

    pyproject = Pyproject(pyproject_str)
    pyproject.update_dependencies(latest=True)
    assert pyproject.dumps() == expected_pyproject_str
    assert (
        pyproject.pyproject["tool"]["poetry"]["dependencies"]["poetryup"]
        == "^0.2.0"
    )


def test_update_dependencies_with_capital_letters(
    mock_poetry_commands,
) -> None:
    pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/input_pyproject/pyproject_with_capital_letters.toml",
        )
    ).read_text()
    expected_pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/expected_pyproject/pyproject_with_capital_letters.toml",
        )
    ).read_text()

    pyproject = Pyproject(pyproject_str)
    pyproject.update_dependencies()
    assert pyproject.dumps() == expected_pyproject_str
    assert (
        pyproject.pyproject["tool"]["poetry"]["dependencies"]["PoetryUp"]
        == "^0.2.0"
    )


def test_update_dependencies_latest_with_capital_letters(
    mock_poetry_commands,
) -> None:
    pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/input_pyproject/pyproject_with_capital_letters.toml",
        )
    ).read_text()
    expected_pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/expected_pyproject/pyproject_with_capital_letters.toml",
        )
    ).read_text()

    pyproject = Pyproject(pyproject_str)
    pyproject.update_dependencies(latest=True)
    assert pyproject.dumps() == expected_pyproject_str
    assert (
        pyproject.pyproject["tool"]["poetry"]["dependencies"]["PoetryUp"]
        == "^0.2.0"
    )


def test_update_dependencies_with_underscore_character(
    mock_poetry_commands,
) -> None:
    pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/input_pyproject/pyproject_with_underscore_character.toml",
        )
    ).read_text()
    expected_pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/expected_pyproject/",
            "pyproject_with_underscore_character.toml",
        )
    ).read_text()

    pyproject = Pyproject(pyproject_str)
    pyproject.update_dependencies()
    assert pyproject.dumps() == expected_pyproject_str
    assert (
        pyproject.pyproject["tool"]["poetry"]["dependencies"]["poetryup_extra"]
        == "^0.2.0"
    )


def test_update_dependencies_latest_with_underscore_character(
    mock_poetry_commands,
) -> None:
    pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/input_pyproject/",
            "pyproject_with_underscore_character.toml",
        )
    ).read_text()
    expected_pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/expected_pyproject/",
            "pyproject_with_underscore_character.toml",
        )
    ).read_text()

    pyproject = Pyproject(pyproject_str)
    pyproject.update_dependencies(latest=True)
    assert pyproject.dumps() == expected_pyproject_str
    assert (
        pyproject.pyproject["tool"]["poetry"]["dependencies"]["poetryup_extra"]
        == "^0.2.0"
    )


def test_update_dependencies_with_dependency_groups(
    mock_poetry_commands,
) -> None:
    pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/input_pyproject/pyproject_with_dependency_groups.toml",
        )
    ).read_text()
    expected_pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/expected_pyproject/pyproject_with_dependency_groups.toml",
        )
    ).read_text()

    pyproject = Pyproject(pyproject_str)
    pyproject.update_dependencies()
    assert pyproject.dumps() == expected_pyproject_str
    assert (
        pyproject.pyproject["tool"]["poetry"]["group"]["main"]["dependencies"][
            "poetryup"
        ]
        == "^0.2.0"
    )


def test_update_dependencies_latest_with_dependency_groups(
    mock_poetry_commands,
) -> None:
    pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/input_pyproject/pyproject_with_dependency_groups.toml",
        )
    ).read_text()
    expected_pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/expected_pyproject/pyproject_with_dependency_groups.toml",
        )
    ).read_text()

    pyproject = Pyproject(pyproject_str)
    pyproject.update_dependencies(latest=True)
    assert pyproject.dumps() == expected_pyproject_str
    assert (
        pyproject.pyproject["tool"]["poetry"]["group"]["main"]["dependencies"][
            "poetryup"
        ]
        == "^0.2.0"
    )


def test_update_dependencies_with_exact_version_dependency(
    mock_poetry_commands,
) -> None:
    pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/input_pyproject/",
            "pyproject_with_exact_version_dependency.toml",
        )
    ).read_text()
    expected_pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/expected_pyproject/",
            "pyproject_with_exact_version_dependency.toml",
        )
    ).read_text()

    pyproject = Pyproject(pyproject_str)
    pyproject.update_dependencies()
    assert pyproject.dumps() == expected_pyproject_str
    assert (
        pyproject.pyproject["tool"]["poetry"]["dependencies"]["poetryup"]
        == "0.2.0"
    )


def test_update_dependencies_latest_with_exact_version_dependency(
    mock_poetry_commands,
) -> None:
    pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/input_pyproject/",
            "pyproject_with_exact_version_dependency.toml",
        )
    ).read_text()
    expected_pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/expected_pyproject/",
            "pyproject_with_exact_version_dependency.toml",
        )
    ).read_text()

    pyproject = Pyproject(pyproject_str)
    pyproject.update_dependencies(latest=True)
    assert pyproject.dumps() == expected_pyproject_str
    assert (
        pyproject.pyproject["tool"]["poetry"]["dependencies"]["poetryup"]
        == "0.2.0"
    )


def test_update_dependencies_latest_skip_exact_with_exact_version_dependency(
    mock_poetry_commands,
    mocker: MockerFixture,
) -> None:
    pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/input_pyproject/",
            "pyproject_with_exact_version_dependency.toml",
        )
    ).read_text()

    mocker.patch.object(
        Pyproject,
        "_Pyproject__run_poetry_show",
        return_value=(
            "poetryup 0.1.0 Update dependencies and bump their version in the "
            "pyproject.toml file"
            "\n└── toml >=0.10.2,<0.11.0\n"
        ),
    )

    pyproject = Pyproject(pyproject_str)
    pyproject.update_dependencies(latest=True)
    assert (
        pyproject.pyproject["tool"]["poetry"]["dependencies"]["poetryup"]
        == "0.1.0"
    )


def test_update_dependencies_with_git_dependency(
    mock_poetry_commands,
) -> None:
    pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/input_pyproject/pyproject_with_git_dependency.toml",
        )
    ).read_text()
    expected_pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/expected_pyproject/pyproject_with_git_dependency.toml",
        )
    ).read_text()

    pyproject = Pyproject(pyproject_str)
    pyproject.update_dependencies()
    assert pyproject.dumps() == expected_pyproject_str
    assert (
        pyproject.pyproject["tool"]["poetry"]["dependencies"]["poetryup"]["git"]
        == "https://github.com/MousaZeidBaker/poetryup.git"
    )


def test_update_dependencies_latest_with_git_dependency(
    mock_poetry_commands,
) -> None:
    pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/input_pyproject/pyproject_with_git_dependency.toml",
        )
    ).read_text()
    expected_pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/expected_pyproject/pyproject_with_git_dependency.toml",
        )
    ).read_text()

    pyproject = Pyproject(pyproject_str)
    pyproject.update_dependencies(latest=True)
    assert pyproject.dumps() == expected_pyproject_str
    assert (
        pyproject.pyproject["tool"]["poetry"]["dependencies"]["poetryup"]["git"]
        == "https://github.com/MousaZeidBaker/poetryup.git"
    )


def test_update_dependencies_with_restricted_dependency(
    mock_poetry_commands,
) -> None:
    pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/input_pyproject/",
            "pyproject_with_restricted_dependency.toml",
        )
    ).read_text()
    expected_pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/expected_pyproject/",
            "pyproject_with_restricted_dependency.toml",
        )
    ).read_text()

    pyproject = Pyproject(pyproject_str)
    pyproject.update_dependencies()
    assert pyproject.dumps() == expected_pyproject_str
    assert (
        pyproject.pyproject["tool"]["poetry"]["dependencies"]["poetryup"][
            "version"
        ]
        == "^0.2.0"
    )


def test_update_dependencies_latest_with_restricted_dependency(
    mock_poetry_commands,
) -> None:
    pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/input_pyproject/",
            "pyproject_with_restricted_dependency.toml",
        )
    ).read_text()
    expected_pyproject_str = Path(
        os.path.join(
            os.path.dirname(__file__),
            "fixtures/expected_pyproject/",
            "pyproject_with_restricted_dependency.toml",
        )
    ).read_text()

    pyproject = Pyproject(pyproject_str)
    pyproject.update_dependencies(latest=True)
    assert pyproject.dumps() == expected_pyproject_str
    assert (
        pyproject.pyproject["tool"]["poetry"]["dependencies"]["poetryup"][
            "version"
        ]
        == "^0.2.0"
    )
