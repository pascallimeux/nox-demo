# noxfile.py
import nox

SOURCE_FILES = (
    "noxfile.py",
    "mylib/",
    "tests/",
)

PYTHON_VERSION = "3.9"
nox.options.sessions = "format", "test"


@nox.session(python=PYTHON_VERSION)
def format(session: nox.Session) -> None:
    """Formatage du code Python"""
    args = session.posargs or SOURCE_FILES
    session.install("black", "isort")
    session.run("isort", "--profile=black", *args)
    session.run("black", *args)
    lint(session)


@nox.session(python=PYTHON_VERSION)
def lint(session: nox.Session) -> None:
    """Analyse statique du code Python."""
    args = session.posargs or SOURCE_FILES
    session.install("flake8", "black", "mypy", "isort", "safety")
    session.run("isort", "--check", "--profile=black", *args)
    session.run("black", "--check", *args)
    session.run("flake8", *args)
    session.run("mypy", *args)
    session.run("safety", "check", "--file=requirements.txt", "--full-report")


@nox.session(python=PYTHON_VERSION)
def test(session: nox.Session) -> None:
    """Exécution de la suite de tests."""
    args = session.posargs or ["--cov"]
    session.install("-r", "requirements.txt")
    session.install("pytest", "pytest-cov")
    session.run("pytest", *args)


@nox.session(python=PYTHON_VERSION)
def package(session: nox.Session) -> None:
    """Création du package."""
    session.install(".")
    session.run("python", "setup.py", "sdist", "--formats=zip")


@nox.session(python=PYTHON_VERSION)
def docs(session: nox.Session) -> None:
    """Construction de la documentation."""
    session.install("sphinx", "sphinx-autodoc-typehints", "sphinx-rtd-theme")
    session.run("sphinx-build", "docs", "docs/_build")
