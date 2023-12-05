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

# tags = ['V1.0','V2.0','V3.0','V4.0','V5.0']
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Configure sphinx-multiversion
# smv_tag_whitelist = r'^v\d+\.\d+$'
# smv_branch_whitelist = r'^main$'
#
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode','sphinx_versioning','sphinx_multiversion']
# extensions = ['sphinx_multiversion']


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
        'page.html'
        # 'versions_and_tags.html',
        'searchbox.html',
        'globaltoc.html', 'relations.html',
        'sourcelink.html'
    ],
}

# html_theme_options = {
#     "versions": {"latest": "/latest", "v1.0": "/v1.0", "v2.0": "/v2.0"},
#     "prev_next_buttons_location": "both",
#     "style_external_links": True,
#     "navigation_depth": 4,
#     "includehidden": True,
#     "titles_only": False,
#     "display_version_dropdown": True,
#     "version_dropdown_title": "Versions & Tags",
#     "version_dropdown": "versions_and_tags.html",
# }
html_theme = 'classic'
html_static_path = ['_static']


# Whitelist pattern for tags (set to None to ignore all tags)
smv_tag_whitelist = r'^.*$'

# Whitelist pattern for branches (set to None to ignore all branches)
# smv_branch_whitelist = r'^.*$'

# Whitelist pattern for remotes (set to None to use local branches only)
# smv_remote_whitelist = None

# Pattern for released versions
# smv_released_pattern = r'^tags/.*$'

# Format for versioned output directories inside the build directory
smv_outputdir_format = '{ref.name}'

# Determines whether remote or local git branches/tags are preferred if their output dirs conflict
# smv_prefer_remote_refs = False


# smv_tag_whitelist = r'^.*$'                   # Include all tags
# smv_tag_whitelist = r'^v\d+\.\d+$'            # Include tags like "v2.1"

# smv_branch_whitelist = r'^.*$'                # Include all branches
# smv_branch_whitelist = r'^(?!master).*$'      # Include all branches except "master"

# smv_remote_whitelist = None                   # Only use local branches
# smv_remote_whitelist = r'^.*$'                # Use branches from all remotes
# smv_remote_whitelist = r'^(origin|upstream)$' # Use branches from origin and upstream

# smv_released_pattern = r'^tags/.*$'           # Tags only
# smv_released_pattern = r'^heads/\d+\.\d+$'    # Branches like "2.1"
# smv_released_pattern = r'^(tags/.*|heads/\d+\.\d+)$'           # Branches like "2.1" and all tags
# smv_released_pattern = r'^(heads|remotes/[^/]+)/(?!:master).*$' # Everything except master branch

