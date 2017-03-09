'''
constants.py
Generates constants for use in blinkpy
'''
MAJOR_VERSION = 0
MINOR_VERSION = 4
PATCH_VERSION = 4
__version__ = '{}.{}.{}'.format(MAJOR_VERSION, MINOR_VERSION, PATCH_VERSION)

REQUIRED_PYTHON_VER = (3, 4, 2)

PROJECT_NAME = 'blinkpy'
PROJECT_PACKAGE_NAME = 'blinkpy'
PROJECT_LICENSE = 'MIT'
PROJECT_AUTHOR = 'Kevin Fronczak'
PROJECT_COPYRIGHT = ' 2017, {}'.format(PROJECT_AUTHOR)
PROJECT_URL = 'https://github.com/fronzbot/blinkpy'
PROJECT_EMAIL = 'kfronczak@gmail.com'
PROJECT_DESCRIPTION = ('A Blink camera Python library '
                       'running on Python 3.')
PROJECT_LONG_DESCRIPTION = ('blinkpy is an open-source '
                            'unofficial API for the Blink Camera '
                            'system with the intention for easy '
                            'integration into various home '
                            'automation platforms.')
PROJECT_CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.4',
    'Topic :: Home Automation'
]

PROJECT_GITHUB_USERNAME = 'home-assistant'
PROJECT_GITHUB_REPOSITORY = 'home-assistant'

PYPI_URL = 'https://pypi.python.org/pypi/{}'.format(PROJECT_PACKAGE_NAME)

'''
URLS
'''
BLINK_URL = 'immedia-semi.com'
LOGIN_URL = 'https://prod.' + BLINK_URL + '/login'
BASE_URL = 'https://prod.' + BLINK_URL
DEFAULT_URL = 'prod.' + BLINK_URL
HOME_URL = BASE_URL + '/homescreen'
EVENT_URL = BASE_URL + '/events/network/'
NETWORK_URL = BASE_URL + '/network/'
NETWORKS_URL = BASE_URL + '/networks'

'''
Dictionaries
'''
ONLINE = {'online': True, 'offline': False}