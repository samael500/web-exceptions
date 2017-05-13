# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from dj_exceptions.urls import urlpatterns as dj_exceptions_urls

urlpatterns = [
    url(r'^', include(dj_exceptions_urls, namespace='dj_exceptions')),
]
