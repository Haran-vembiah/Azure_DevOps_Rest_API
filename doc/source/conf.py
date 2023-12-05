# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sphinx_multiversion


project = 'Test automation'
copyright = '2023, Haran'
author = 'Haran'
release = 'Orion'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

tags = ['V1.0','V2.0','V3.0','V4.0','V5.0']
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Configure sphinx-multiversion
smv_tag_whitelist = r'^v\d+\.\d+$'
smv_branch_whitelist = r'^main$'

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode','sphinx_multiversion']

templates_path = ['_templates']
exclude_patterns = []

language = 'En'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
