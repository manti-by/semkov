from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

SECRET_KEY = "insecure-key"

ALLOWED_HOSTS = ("127.0.0.1",)

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
