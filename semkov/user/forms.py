from django import forms

from wagtail.users.forms import UserEditForm, UserCreationForm


class CustomUserEditForm(UserEditForm):
    identifier = forms.CharField(required=True)
    ip_address = forms.GenericIPAddressField()


class CustomUserCreationForm(UserCreationForm):
    identifier = forms.CharField(required=True)
    ip_address = forms.GenericIPAddressField()
