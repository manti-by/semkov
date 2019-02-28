from django.utils import translation


class LocaleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if "django" in request.path:
            locale = "en"
        else:
            locale = "ru"

        translation.activate(locale)
        request.LANGUAGE_CODE = translation.get_language()

        response = self.get_response(request)
        translation.deactivate()

        return response
