from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from semkov.user.models import User

admin.register(User, UserAdmin)
