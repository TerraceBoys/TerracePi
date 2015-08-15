__author__ = 'mark'

import os
import logging

APP_ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
DEBUG = os.environ['SERVER_SOFTWARE'].startswith('Dev')
logging.info("Starting application in DEBUG mode: %s", DEBUG)