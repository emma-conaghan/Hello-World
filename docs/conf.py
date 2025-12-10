# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------

project = 'Hello World Project'
copyright = '2025, Emma Conaghan'
author = 'Emma Conaghan'
release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Make Sphinx use index.rst as homepage
root_doc = 'index'

# -- Options for HTML output -------------------------------------------------

html_theme = "furo"

# Remove warning: folder doesn't exist
html_static_path = []
