project = 'SL API'
copyright = '2025, Social Links'
author = 'Social Links'

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_show_sourcelink = False
html_logo = "img/logo.svg"
html_theme_options = {
    'logo_only': True,
}

html_css_files = [
    'custom.css',
]