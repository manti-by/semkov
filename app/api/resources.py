import json
import logging

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.utils.translation import ugettext_lazy as _
from djrest.resource import Resource
from wagtail.core.models import Page

from ads.models import AdsModel
from api.utils import resource_wrapper
from core.models import Email

logger = logging.getLogger()


class ContactResource(Resource):
    @resource_wrapper
    def post(self, request):
        meta = {}
        for item in ["HTTP_ACCEPT_LANGUAGE", "HTTP_REFERER", "HTTP_USER_AGENT"]:
            meta[item] = request.META.get(item)

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


class AdsResource(Resource):
    @resource_wrapper
    def post(self, request):
        if not request.user.is_authenticated:
            return JsonResponse(
                {
                    "status": 403,
                    "message": _("Please login first"),
                },
                status=200,
            )

        ads_category = Page.objects.get(slug='ads')
        ads_page = AdsModel(title=request.POST.get("title"), text=request.POST.get("text"),
                            owner=request.user, live=False)
        ads_category.add_child(instance=ads_page)
        ads_page.save()
        return JsonResponse(
            {
                "status": 200,
                "message": _("Thanks for submission, we'll post it after moderation"),
            },
            status=200,
        )


class LoginResource(Resource):
    @resource_wrapper
    def post(self, request):
        if request.user.is_authenticated:
            return JsonResponse(
                {
                    "status": 400,
                    "message": _("Already logged in"),
                },
                status=200,
            )

        user = authenticate(
            username=request.POST.get("email"), password=request.POST.get("password")
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
        return JsonResponse(
            {
                "status": 200,
                "message": _("Successfully logged in"),
            },
            status=200,
        )
