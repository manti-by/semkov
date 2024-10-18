from django.urls import path

from semkov.api.views import (
    ads_view,
    contact_view,
    login_view,
    logout_view,
    register_view,
)


app_name = "api"

urlpatterns = [
    path("contact/", contact_view, name="contact"),
    path("ads/", ads_view, name="ads"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
