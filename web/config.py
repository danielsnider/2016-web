import os


class Config(object):
    DEBUG = True

    # Paths
    APP_PATH = os.path.dirname(os.path.abspath(__file__))
    STATIC_PATH = os.path.join(APP_PATH, 'static')

    # i18n Config
    LANGUAGES = {
        'en': 'English',
        'fr': 'Francais'
    }

    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

    # Destination of the build directory
    FREEZER_DESTINATION = os.path.join(APP_PATH, '../build/')
    FREEZER_IGNORE_404_NOT_FOUND = True

    MARKDOWN_EXTENSION_CONFIG = {}
