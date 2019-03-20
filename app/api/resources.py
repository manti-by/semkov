import json
import logging

from django.http import JsonResponse
from django.utils.translation import ugettext_lazy as _
from djrest.resource import Resource

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
        return JsonResponse(
            {
                "status": 200,
                "message": _("Thanks for submission, we'll get in touch soon"),
            },
            status=200,
        )
