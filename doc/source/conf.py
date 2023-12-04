# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Test documentation'
copyright = '2023, Haran'
author = 'Haran'
release = 'Sample project'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'sphinx_markdown_builder', 'sphinx_versioning']
versions = ['V1.0', 'v1.1', 'v2.0']

# The short X.Y version.
versions = ['V1.0', 'v1.1', 'v2.0']
# The full version, including alpha/beta/rc tags.
html_context = {
    'versions': versions,
    'current_version': 'V1.0',
    'urls': {
        'v1.0': 'https://example.com/docs/v1.0/',
        'v1.1': 'https://example.com/docs/v1.1/',
        'v2.0': 'https://example.com/docs/v2.0/',
    },
}

# html_theme_options = {
#     'version_dropdown': True,
#     'versions': versions,
#     'current_version': 'V1.0',
#     'dropdown_title': 'Versions',
# }
# # scm_version_options = {
#     'git': '--tags --abbrev=10 --dirty=-d'
# }
# sphinx_versioning.versioning(
#     "My Project",
#     "../../",
#     "docs/",
#     versions=["latest", "V1.0"],
#     default_version="V1.0",
#     # base_url="https://myproject.com/docs/",
#     static_path=["_static"],
#     ignore=["venv"],
#     overwrite=True,
# )

# versions = {
#     'latest', 'latest',
#     'V1.0': 'V1.0',
#     '2.0': 'v2.0',
#     'master': 'main'
# }

pygments_style = 'native'

# Some useful configurations:
autoclass_content = "both"  # Include both the class's and the init's docstrings.
autodoc_member_order = 'bysource'  # In the documentation, keep the same order of members as in the code.
autodoc_default_flags = ['members']  # Default: include the docstrings of all the class/module members.
# ------- end of user configured ----------------
html_add_permalinks = ''

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
autosectionlabel_prefix_document = True
markdown_ext = ['.md']
source_suffix = ['.rst', '.md']
# html_theme = 'alabaster'
# html_theme = 'classic'
html_sidebars = {
    '**': [
        # ... other sidebars ...
        # Suggest putting the extension above the search bar for better UX.
        # 'sidebar/sphinx_versioning.html',
        'searchbox.html',
        'globaltoc.html', 'relations.html',
        'sourcelink.html'
    ]
}
html_theme = 'classic'
html_static_path = ['_static']
htmlhelp_basename = 'G5 Orion Test automation'


# -- Add custom roles --------------------------------------------------------
#
# def external_link_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
#     app = inliner.document.settings.env.app
#     config = app.config
#     base_url = config.external_link_base_url
#     ref = f"{base_url}{text} 🌐"
#     node = nodes.reference(rawtext, ref, **options)
#     return [node], []
#
#
# roles.register_local_role('external-link', external_link_role)
#
#
# def keyword_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
#     keywords = [word.strip() for word in text.split(',')]
#
#     # Creating a list to hold nodes
#     node_list = []
#     for i, keyword in enumerate(keywords):
#         # Emphasize (italicize) each keyword.
#         node_list.append(nodes.emphasis(rawtext, keyword))
#
#         # If it is not the last keyword, add a comma and a space.
#         if i < len(keywords) - 1:
#             node_list.append(nodes.Text(', ', ', '))
#
#     # Returning the node list.
#     return node_list, []
#
#
# # Register the role.
# roles.register_local_role('keywords', keyword_role)
# def setup(app):
#     versioning_setup(app)
# sphinx_versioning.versioning(
#     "My Project",
#     "../../",
#     "docs/",
#     versions=["latest", "v1.0"],
#     default_version="latest",
#     base_url="https://myproject.com/docs/",
#     static_path=["_static"],
#     ignore=["venv"],
#     overwrite=True,
# )
# def setup(app):
#     sphinx_versioning.versioning(
#         app=app,
#         versions=["latest", "v1.0"],
#         base_dir="../../",
#         src_dir="docs/source/",
#         dest_dir="docs/build/",
#         default_version="latest",
#         style="navbar",
#         banner_location="top",
#         static_path=["_static"],
#         version_dropdown=True,
#         ignore=["venv"],
#         overwrite=True,
#     )


