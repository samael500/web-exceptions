# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import
from django.conf.urls import url

from tests import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
]

handler444 = views.handler444
