from .settings import *
import os.path

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['107.20.130.227', 'localhost']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')