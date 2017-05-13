# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from web_exceptions.urls import urlpatterns as web_exceptions_urls

urlpatterns = [
    url(r'^', include(web_exceptions_urls, namespace='web_exceptions')),
]
