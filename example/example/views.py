from django.http import HttpResponse
from web_exceptions import exceptions


class HTTPTeapot(exceptions.HTTPClientError):
    status_code = 418
    reason = "I'm a teapot"


def index(request):
    """ Simple view raise exception """
    raise exceptions.HTTPOk(
        content="Thist is Http Ok response",
        headers={'X-Extra-Header': 'some value'})


def tea(request):
    """ Raise teapot exception """
    raise HTTPTeapot()


def coffee(request):
    """ Raise redirect to a teapot exception """
    raise exceptions.HTTPMovedPermanently('/tea')


def timeout(request):
    """ Raise 408 to return handler408 """
    raise exceptions.HTTPRequestTimeout()


def handler408(request):
    """ Custom response handler """
    return HttpResponse(content="Custom 408 handler", status=408)
