import os
import sys
sys.path.insert(0, os.path.abspath('.'))
from cechmate import __version__
from sktda_docs_config import *


project = u'Cechmate'
copyright = u'2019, Chris Tralie and Nathaniel Saul'
author = u'Chris Tralie and Nathaniel Saul'

version = __version__
release = __version__

html_theme_options.update({
  # Google Analytics info
  'ga_ua': 'UA-124965309-5',
  'ga_domain': '',
  'gh_url': 'scikit-tda/cechmate'
})
html_short_title = project
htmlhelp_basename = 'cechmatedoc'