"""Sphinx configuration."""
project = "fib-calc"
author = "pascal Limeux"
copyright = f"2022, {author}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx_rtd_theme",
]

html_theme = "sphinx_rtd_theme"
