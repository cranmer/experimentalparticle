#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'NYU Experimental Particle Group'
SITENAME = u'Experimental Particle Physics at NYU'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

#ARTICLE_URL = ''
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU=False

BOOTSTRAP_NAVBAR_INVERSE =True

#BANNER='images/banner.png'
#BANNER_SUBTITLE = 'This is my subtitle'

DISPLAY_ARTICLE_INFO_ON_INDEX=False
DISPLAY_TAGS_ON_SIDEBAR=True
DISPLAY_RECENT_POSTS_ON_SIDEBAR=True



MENUITEMS = (
			('People','/group.html'),
			('Research','/research.html'),
			('Publications','/publications.html'),
			('Funding','/funding.html'),
			('Media & Outreach','/outreach.html'),)

# Blogroll
LINKS =  (('NYU Physics Department','http://physics.as.nyu.edu/page/home'),
		('ATLAS','http://atlas.web.cern.ch'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

####################################################
# Additions 
STATIC_PATHS = ['images', 'images/med', 'downloads', 'downloads/notebooks',
                'downloads/files','downloads/code', 'favicon.png']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'pelican-bootstrap3'
#THEME = 'notmyidea'
PYGMENTS_STYLE='default'
#PYGMENTS_STYLE='friendly'
#THEME = '../pelican-bootstrap3'
#THEME = '/Users/cranmer/virtualenvs/pelican/lib/python2.7/site-packages/pelican/themes/pelican-bootstrap3'
# This requires Pelican 3.3+

#For pelican-ootstrap3
BOOTSTRAP_THEME='simplex'
BOOTSTRAP_THEME='yeti'
#BOOTSTRAP_THEME='superhero' #nice but, background doesn't work well with code as is
#BOOTSTRAP_THEME='cosmo'