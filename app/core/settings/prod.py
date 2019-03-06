from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

COMPRESS_ENABLED = True

SECRET_KEY = "m51kjn1%w(re&a^ez%kk4&y^$tccpnz%#t7)_g)p(9sq(6*gvc"

ALLOWED_HOSTS = ["127.0.0.1", "sg.manti.by"]

try:
    from .local import *
except ImportError:
    pass
