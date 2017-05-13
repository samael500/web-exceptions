from django.http import HttpResponse
from django.views.generic import View


class IndexView(View):

    """ Simple view for test """

    def get(self, *args, **kwargs):
        return HttpResponse(content="Thist is default view response")
