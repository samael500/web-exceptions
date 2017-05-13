from web_exceptions.exceptions import HTTPException
from django.core import urlresolvers


class WebExceptionsMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response
        self.url_handlers = urlresolvers.get_resolver().urlconf_module

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if not isinstance(exception, HTTPException):
            return
        handler = getattr(self.url_handlers, 'handler{}'.format(
            exception.status_code), None)
        if callable(handler):
            return handler(request)
        return exception
