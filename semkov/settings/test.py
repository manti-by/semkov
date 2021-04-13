from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

COMPRESS_ENABLED = True

SECRET_KEY = "m51kjn1%w(re&a^ez%kk4&y^$tccpnz%#t7)_g)p(9sq(6*gvc"

ALLOWED_HOSTS = ["127.0.0.1"]

STATIC_ROOT = "/srv/semkov/static"
MEDIA_ROOT = "/srv/semkov/media"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s [%(levelname)s] %(message)s",
            "datefmt": "%H:%M:%S",
        }
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
            "formatter": "simple",
        },
        "django": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": True,
            "formatter": "simple",
        },
        "wagtail": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": True,
            "formatter": "simple",
        },
    },
}
