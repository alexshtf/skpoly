"""Sphinx configuration for the skpoly documentation."""

from __future__ import annotations

import sys
from importlib.metadata import PackageNotFoundError, version as get_version
from pathlib import Path


DOCS_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = DOCS_ROOT.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))


project = "skpoly"
author = "Alex Shtoff"

try:
    release = get_version("skpoly")
except PackageNotFoundError:  # pragma: no cover - package may be editable install
    release = "0.1.0"


version = release

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

autosummary_generate = True
autodoc_default_options = {
    "members": True,
    "inherited-members": True,
    "show-inheritance": True,
}
autodoc_typehints = "description"

napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_param = True
napoleon_use_rtype = True

templates_path: list[str] = []
exclude_patterns = ["_build"]

html_theme = "alabaster"
html_static_path: list[str] = []
