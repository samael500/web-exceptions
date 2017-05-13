from web_exceptions import exceptions


class HTTPTeapot(exceptions.HTTPClientError):
    status_code = 418


def index(request):
    """ Simple view raise exception """
    raise exceptions.HTTPOk(
        content="Thist is Http Ok response",
        headers={'X-Extra-Header': 'some value'})


def tea(request):
    """ Raise teapot exception """
    raise HTTPTeapot(reason="I'm a teapot")


def coffee(request):
    """ Raise redirect to a teapot exception """
    raise exceptions.HTTPMovedPermanently('/tea')
