from .base import *

DEBUG = True

SECRET_KEY = "m51kjn1%w(re&a^ez%kk4&y^$tccpnz%#t7)_g)p(9sq(6*gvc"

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"level": "DEBUG", "class": "logging.StreamHandler"},
        "null": {"class": "logging.NullHandler"},
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
            "formatter": "verbose",
        },
        "django": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": True,
            "formatter": "simple",
        },
        "django.template": {"handlers": ["null"]},
        "django.db.backends": {"handlers": ["null"]},
    },
}

try:
    from .local import *
except ImportError:
    pass
