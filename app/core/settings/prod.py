from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

COMPRESS_ENABLED = True

SECRET_KEY = "m51kjn1%w(re&a^ez%kk4&y^$tccpnz%#t7)_g)p(9sq(6*gvc"

ALLOWED_HOSTS = ["127.0.0.1", "sg.manti.by"]

STATIC_ROOT = "/srv/semkov/static"
MEDIA_ROOT = "/srv/semkov/src/app/media"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/var/log/semkov/app.log",
        },
        "console": {"level": "DEBUG", "class": "logging.StreamHandler"},
        "null": {"class": "logging.NullHandler"},
    },
    "loggers": {
        "": {
            "handlers": ["file"],
            "level": "WARNING",
            "propagate": True,
            "formatter": "verbose",
        },
        "django": {
            "handlers": ["file"],
            "level": "WARNING",
            "propagate": True,
            "formatter": "simple",
        },
        "django.template": {"handlers": ["null"]},
        "django.db.backends": {"handlers": ["null"]},
    },
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "localhost"
EMAIL_PORT = 25

try:
    from .local import *
except ImportError:
    pass
