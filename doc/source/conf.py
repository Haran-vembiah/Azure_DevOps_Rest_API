# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import sphinx_multiversion


sys.path.insert(0, os.path.abspath('.'))

project = 'Test automation'
copyright = '2023, Haran'
author = 'Haran'
release = 'Orion'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode','sphinx_versioning','sphinx_multiversion']

# Set up sphinx-multiversion
smv_tag_whitelist = r'^.*$'
smv_branch_whitelist = r'^main$'
smv_remote_whitelist = r'^origin$'
smv_latest_version = 'main'
smv_show_banner = True
smv_versions = [release]
smv_branch_strategy = 'independent'

# exclude_patterns = []

language = 'En'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

templates_path = [
    "_templates",
]
html_sidebars = {
    '**': [
        'versioning.html',
        # 'page.html',
        # 'versions_and_tags.html',
        'searchbox.html',
        'globaltoc.html',
        'relations.html',
        'sourcelink.html',
    ],
}

html_theme = 'classic'
html_static_path = ['_static']

# Format for versioned output directories inside the build directory
smv_outputdir_format = '{ref.name}'