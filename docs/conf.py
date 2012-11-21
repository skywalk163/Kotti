# -*- coding: utf-8 -*-
#
# Kotti documentation build configuration file, created by
# sphinx-quickstart on Fri Mar 18 23:14:47 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

#import os
#import sys

#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

#needs_sphinx = '1.0'
extensions = [
    'repoze.sphinx.autointerface',
    'sphinx.ext.autodoc',
    'sphinx.ext.graphviz',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.viewcode',
    ]

templates_path = ['_templates']
source_suffix = '.rst'
#source_encoding = 'utf-8-sig'
master_doc = 'index'
project = u'Kotti'
copyright = u'2012, Daniel Nouri and contributors'
version = '0.8'
# The full version, including alpha/beta/rc tags.
release = version
#language = None
today_fmt = '%Y-%m-%d'
exclude_patterns = ['_build', '_themes']
#default_role = None
#add_function_parentheses = True
#add_module_names = True
#show_authors = False
pygments_style = 'sphinx'
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

html_theme_path = ['_themes']
html_theme = 'sphinxtheme_bootstrap'
html_theme_options = {
    'github_user': 'Pylons',
    'github_repo': 'Kotti',
    'twitter_username': 'KottiCMS',
    'home_url': 'http://kotti.pylonsproject.org/',
    'mailing_list_url': 'http://groups.google.com/group/kotti',
    'irc_channel_url': 'irc://irc.freenode.net/#kotti',
}
# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None
# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None
#html_logo = None
#html_favicon = None
html_static_path = ['_static']
html_last_updated_fmt = '%Y-%m-%d'
#html_use_smartypants = True
#html_sidebars = {}
#html_additional_pages = {}
#html_domain_indices = True
#html_use_index = True
#html_split_index = False
#html_show_sourcelink = True
#html_show_sphinx = True
#html_show_copyright = True
#html_use_opensearch = ''
#html_file_suffix = None
htmlhelp_basename = 'Kottidoc'


# -- Options for LaTeX output --------------------------------------------------

#latex_paper_size = 'a4'
#latex_font_size = '10pt'
latex_documents = [
  ('index', 'Kotti.tex', u'Kotti Documentation',
   u'Daniel Nouri', 'manual'),
]
#latex_logo = None
#latex_use_parts = False
#latex_show_pagerefs = False
#latex_show_urls = False
#latex_preamble = ''
#latex_appendices = []
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'kotti', u'Kotti Documentation', [u'Daniel Nouri'], 1)
]

# -- Options for inheritance diagrams ------------------------------------------
inheritance_graph_attrs = dict(rankdir='TB', nodesep=0.1,
                               ratio='auto', size=11.0)
inheritance_node_attrs = dict(height=0.7, margin='0.06, 0.03')

# -- Options for Intersphinx ---------------------------------------------------
intersphinx_mapping = {
    'colander': ('http://python.readthedocs.org/en/latest/', None),
    'deform': ('http://deform.readthedocs.org/en/latest/', None),
    'pyramid': ('http://pyramid.readthedocs.org/en/latest/', None),
    'sqlalchemy': ('http://sqlalchemy.readthedocs.org/en/latest/', None),
}
