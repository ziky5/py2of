"""Sphinx configuration."""
project = "Ultimate PyFoam"
author = "Andrej Rostek"
copyright = "2022, Andrej Rostek"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
