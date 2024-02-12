import json
import logging

from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from wagtail.models import Page

from semkov.apps.ads.models import AdsModel
from semkov.apps.core.models import Email
from semkov.apps.core.services.recaptcha import is_valid_recaptcha_token
from semkov.apps.user.models import User

logger = logging.getLogger(__name__)


def contact_view(request):
    meta = {}
    for item in ["HTTP_ACCEPT_LANGUAGE", "HTTP_REFERER", "HTTP_USER_AGENT"]:
        meta[item] = request.META.get(item)

    if not is_valid_recaptcha_token(request.POST.get("token")):
        return JsonResponse(
            {
                "message": _("ReCaptcha token is invalid"),
            },
            status=403,
        )

    e = Email(
        name=request.POST.get("name"),
        contact=request.POST.get("contact"),
        subject=_("Submission request from Semkov app"),
        message=request.POST.get("message"),
        meta=json.dumps({"cookies": request.COOKIES, "meta": meta}),
    )
    e.save()
    return JsonResponse(
        {
            "status": 200,
            "message": _("Thanks for submission, we'll get in touch soon"),
        },
        status=200,
    )


def ads_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"status": 403, "message": _("Please login first")}, status=200)

    ads_category = Page.objects.get(slug="ads")
    ads_page = AdsModel(
        title=request.POST.get("title"),
        text=request.POST.get("text"),
        owner=request.user,
        live=False,
    )
    ads_category.add_child(instance=ads_page)
    ads_page.save()
    return JsonResponse(
        {
            "status": 200,
            "message": _("Thanks for submission, we'll post it after moderation"),
        },
        status=200,
    )


def register_view(request):
    if request.user.is_authenticated:
        return JsonResponse({"status": 400, "message": _("Already logged in")}, status=200)

    ip_address = request.META.get("REMOTE_ADDR")
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip_address = x_forwarded_for.split(",")[-1].strip()

    user = User(
        identifier=request.POST.get("identifier"),
        ip_address=ip_address,
    )
    user.set_password(request.POST.get("password"))
    user.save()

    return JsonResponse(
        {
            "status": 200,
            "message": _("Account successfully created, please wait for activation"),
        },
        status=200,
    )


def login_view(request):
    if request.user.is_authenticated:
        return JsonResponse({"status": 400, "message": _("Already logged in")}, status=200)

    user = User.authenticate(
        identifier=request.POST.get("identifier"),
        password=request.POST.get("password"),
    )
    if user is None:
        return JsonResponse(
            {
                "status": 403,
                "message": _("Can't find user with provided credentials"),
            },
            status=200,
        )

    login(request, user)
    return JsonResponse({"status": 200, "message": _("Successfully logged in")}, status=200)


def logout_view(request):
    logout(request)
    return JsonResponse({"status": 200, "message": _("Successfully logged out")}, status=200)
