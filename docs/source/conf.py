# Configuration file for Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from pathlib import Path

# -- Path setup --------------------------------------------------------------
# Add project root to sys.path for autodoc
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

# -- Project information -----------------------------------------------------
project = "test-pypi-pru"
copyright = "2026, Alberto Aragoneses"
author = "Alberto Aragoneses"

# Version from pyproject.toml (dynamic)
try:
    from importlib.metadata import version

    release = version("test-pypi-pru")
except Exception:
    import tomllib

    pyproject = Path(__file__).parent.parent.parent / "pyproject.toml"
    with open(pyproject, "rb") as f:
        release = tomllib.load(f)["project"]["version"]

version = release  # Short version (e.g., 0.17.3)

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",  # Auto-generate from docstrings
    "sphinx.ext.napoleon",  # NumPy/Google docstring support
    "sphinx.ext.viewcode",  # [source] links
    "sphinx.ext.intersphinx",  # Links to other projects
    "sphinx.ext.mathjax",  # LaTeX math via MathJax
    "sphinx_autodoc_typehints",  # Type hints in docs
    "sphinx_copybutton",  # Copy code button
    "myst_parser",  # Markdown support
    "sphinx_design",  # Cards, tabs, grids
]

# MyST configuration (Markdown support)
myst_enable_extensions = [
    "colon_fence",  # ::: directive
    "deflist",  # Definition lists
    "fieldlist",  # Field lists
    "attrs_inline",  # {.class} syntax
    "substitution",  # {{ variable }}
]

# Napoleon settings (NumPy docstrings)
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_param = True
napoleon_use_rtype = True

# Autodoc settings
autodoc_typehints = "signature"  # Show in signature, not description
autodoc_member_order = "bysource"

# Templates path
templates_path = ["_templates"]

# Exclude patterns
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "logo": {
        "text": project,
    },
    "github_url": "https://github.com/actuaan/test_pypi_pub",
    "collapse_navigation": True,
    "header_links_before_dropdown": 6,
    "navbar_end": [
        "version-switcher",
        "search-button.html",
        "theme-switcher.html",
        "navbar-icon-links.html",
    ],
    "navbar_persistent": [],
    "show_nav_level": 2,
    "show_toc_level": 2,
    # Version switcher configuration (like NumPy docs)
    "switcher": {
        "json_url": "https://actuaan.github.io/test_pypi_pub/versions.json",
        "version_match": os.getenv("SPHINX_VERSION_MATCH", version),
    },
}

html_title = f"{project} {version}"
html_static_path = ["_static"]
html_css_files = ["custom.css"]  # Custom CSS with Open Sans and Lato fonts
html_context = {"default_mode": "light"}

# -- Options for MathJax (LaTeX math) ----------------------------------------
# MathJax configuration for actuarial notation with custom macros
mathjax3_config = {
    "tex": {
        "inlineMath": [["$", "$"], ["\\(", "\\)"]],
        "displayMath": [["$$", "$$"], ["\\[", "\\]"]],
        "packages": {
            "[]": ["base", "ams", "newcommand", "configmacros"],
            "[+]": ["physics"],
        },
        "macros": {
            # Custom actuarial macros for simplified notation
            # Format: "name": ["definition", num_params]
            "ax": ["\\ddot{a}_{\\overline{#1}|}", 1],  # Annuity due
            "axi": ["\\ddot{a}_{#1}^{(#2)}", 2],  # m-thly annuity
            "sx": ["\\ddot{s}_{\\overline{#1}|}", 1],  # Accumulated value
            "npx": ["{}_{#1}p_{#2}", 2],  # n-year survival prob
            "nqx": ["{}_{#1}q_{#2}", 2],  # n-year death prob
            "ex": ["\\mathring{e}_{#1}", 1],  # Complete life expectancy
            "Ax": ["\\bar{A}_{#1}", 1],  # Continuous insurance
            "vx": ["v^{#1}", 1],  # Discount factor
        },
    },
    "options": {
        "skipHtmlTags": ["script", "noscript", "style", "textarea", "pre", "code"],
    },
    "loader": {
        "load": ["[tex]/physics", "[tex]/ams"],
    },
}

mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"

# -- Intersphinx mapping -----------------------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "pandas": ("https://pandas.pydata.org/docs/", None),
}

# -- sphinx-multiversion Configuration ----------------------------------------
# Similar to mike in MkDocs
smv_tag_whitelist = r"^v\d+\.\d+\.\d+$"  # Only semantic version tags
smv_branch_whitelist = r"^(main|stable)$"  # Branches to document
smv_remote_whitelist = r"^(origin)$"  # Allowed remote
smv_released_pattern = r"^tags/v.*$"  # Release pattern
smv_outputdir_format = "{ref.name}"  # Directory structure

# Version banner settings
smv_latest_version = "latest"  # Alias for latest version
smv_prefer_remote_refs = False  # Use local refs first
