#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'NYU Experimental Particle Group'
SITENAME = u'EPP @ NYU'
SITEURL = ''
SITEURL = 'https://physics.nyu.edu/experimentalparticle'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

#ARTICLE_URL = ''
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU=False

BOOTSTRAP_NAVBAR_INVERSE =True

BANNER='images/lhc_tunnel.jpg'
BANNER='images/atlas-famous-banner.jpeg'
BANNER_TITLE=None
BANNER_SUBTITLE = 'Experimental Particle Physics @ NYU'
BANNER_ALL_PAGES = True

DISPLAY_ARTICLE_INFO_ON_INDEX=False
DISPLAY_TAGS_ON_SIDEBAR=True
DISPLAY_RECENT_POSTS_ON_SIDEBAR=True


MENUITEMS = (('People','https://physics.nyu.edu/experimentalparticle/group.html'),
			('Research','https://physics.nyu.edu/experimentalparticle/research.html'),
			('Funding','https://physics.nyu.edu/experimentalparticle/funding.html'),
			('Media & Outreach','https://physics.nyu.edu/experimentalparticle/outreach.html'),
			('Blog','https://physics.nyu.edu/experimentalparticle/category/blog.html'),)

MENUITEMS = (('People',SITEURL+'/group.html'),
			('Research',SITEURL+'/research.html'),
			('Funding',SITEURL+'/funding.html'),
			('Media & Outreach',SITEURL+'/outreach.html'),
			('Blog',SITEURL+'/category/blog.html'),)

# Blogroll
LINKS =  (('NYU Physics','http://physics.as.nyu.edu/page/home'),
		#('About the graduate program','http://physics.as.nyu.edu/page/graduate'),
		('The ATLAS Experiment','http://atlas.web.cern.ch'), 
		('Center for Cosmology & Particle Physics','http://cosmo.nyu.edu'),
		('Center for Data Science','http://cds.nyu.edu'),
		#('Overview of our group','overview.html'),
		#('NYU on Milagro', 'milagro.html'),
		#('NYU on ATLAS','atlas.html'),
		#('NYU group history', 'history.html'),
		('RECAST','http://recast.perimeterinstitute.ca'),
		('REANA', 'http://reanahub.io'),
		('DIANA-HEP', 'http://diana-hep.org'),
		('IRIS-HEP', 'http://iris-hep.org'),
		('HiggsHunters', 'http://HiggsHunters.org')
		)

# Social widget
SOCIAL = (('LinkedIn', ''),
          ('Twitter', '#'),)
SOCIAL = None

#SOCIAL = None

DEFAULT_PAGINATION = False
DEFAULT_PAGINATION = 6

CC_LICENSE="CC-BY"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


####################################################
# Additions 
EXTRA_HEADER = open('twitter_card.html').read().decode('utf-8')


STATIC_PATHS = ['images', 'images/med', 'downloads', 'downloads/notebooks',
                'downloads/files','downloads/code', 'favicon.png']

READERS = {'html': None}

CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'


PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
			'liquid_tags.youtube', 'render_math',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal']


#THEME = 'pelican-bootstrap3'
THEME = 'pelican-themes/pelican-bootstrap3'
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

TWITTER_CARDS=True
USE_OPEN_GRAPH=True
TWITTER_DESCRIPTION='The website for the Experimental Particle Physics @ NYU'
TWITTER_USERNAME='kylecranmer'
OPEN_GRAPH_IMAGE="images/atlas-famous-card.jpeg"


