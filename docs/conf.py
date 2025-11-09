# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Cloud Native IoT'
copyright = '2025, David Fan'
author = 'David Fan'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_nb",
    "sphinx_tabs.tabs",
]

templates_path = ['_templates']
exclude_patterns = [
    'build',
    'docs.egg-info',
    '.tox',
    '.venv',
    'README.md',
]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]

html_theme_options = {
    "logo": {
        "text": "Cloud Native IoT",
        # "image_light": "_static/logo-light.png",
        # "image_dark": "_static/logo-dark.png",
    },
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/Kanaderu/Cloud-Native-IoT",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        }
   ],
   "navbar_start": ["navbar-logo"],
   "navbar_center": ["navbar-nav"],
   "navbar_end": ["navbar-icon-links"],
   "navbar_persistent": ["search-button"]
}

html_sidebars = {
    "**": ["sidebar-nav-bs"]
}