from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = "identifier"
    REQUIRED_FIELDS = ["username", "email"]

    identifier = models.CharField(max_length=254, unique=True)
    ip_address = models.GenericIPAddressField(default="127.0.0.1", blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    @classmethod
    def authenticate(cls, identifier=None, password=None):
        try:
            user = cls.objects.get(identifier=identifier)
            if user.check_password(password):
                return user
        except cls.DoesNotExist:
            return None
