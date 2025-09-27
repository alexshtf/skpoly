"""Sphinx configuration for skpoly documentation."""

from __future__ import annotations

import importlib.metadata
import sys
from datetime import datetime
from pathlib import Path

DOCS_PATH = Path(__file__).resolve().parent
PROJECT_ROOT = DOCS_PATH.parent
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

project = "skpoly"

try:
    release = importlib.metadata.version(project)
except importlib.metadata.PackageNotFoundError:
    import tomllib

    with (PROJECT_ROOT / "pyproject.toml").open("rb") as pyproject_file:
        pyproject = tomllib.load(pyproject_file)
    release = pyproject["project"]["version"]

version = release

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.duration",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
]

autosummary_generate = True
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_param = True
napoleon_use_rtype = True

autodoc_member_order = "bysource"
autodoc_typehints = "description"
autodoc_preserve_defaults = True

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "sklearn": ("https://scikit-learn.org/stable/", None),
}

html_theme = "furo"
html_static_path = ["_static"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_title = "skpoly"
html_show_sourcelink = True
copyright = f"{datetime.now():%Y}, skpoly"
