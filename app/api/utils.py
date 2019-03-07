import logging

from django.http import JsonResponse

logger = logging.getLogger()


def resource_wrapper(f):
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            logger.error(e)
            return JsonResponse({"status": 500, "message": e}, status=200)

    return wrapper
