# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]
if os.getenv('SPELLCHECK'):
    extensions += 'sphinxcontrib.spelling',
    spelling_show_suggestions = True
    spelling_lang = 'en_US'
    spelling_word_list_filename = 'wordlist.txt'

source_suffix = '.rst'
master_doc = 'index'
project = u'Cygnet Documentation'
year = u'2015'
author = u'Cygnus'
copyright = '{0}, {1}'.format(year, author)
version = release = u'0.1.0'
import klink
html_theme = "klink"
html_theme_path = [klink.get_html_theme_path()]
html_theme_options = {
    # 'githuburl': 'https://github.com/cygnus-inc/cygnet-docs/'
}

pygments_style = 'trac'
templates_path = ['.']
html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = True
html_sidebars = {
   '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
}
html_short_title = '%s-%s' % (project, version)
