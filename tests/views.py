from django.http import HttpResponse


def index(request):
    """ Simple view for test """
    raise HttpResponse(content="Thist is default view response")
