from django.urls import path

from semkov.api.resources import (
    ContactResource,
    AdsResource,
    RegisterResource,
    LoginResource,
    LogoutResource,
)

app_name = "api"

urlpatterns = [
    path("contact/", ContactResource.as_view(), name="contact"),
    path("ads/", AdsResource.as_view(), name="ads"),
    path("register/", RegisterResource.as_view(), name="register"),
    path("login/", LoginResource.as_view(), name="login"),
    path("logout/", LogoutResource.as_view(), name="logout"),
]
