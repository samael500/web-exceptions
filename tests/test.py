#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_web-exceptions
------------

Tests for `web-exceptions` models exceptions.
"""

from unittest import mock
from django.test import TestCase
from web_exceptions import exceptions


def mock_view(exception, *args, **kwargs):
    def view(self, request):
        raise exception(*args, **kwargs)
    return view


class TestWebExceptions200(TestCase):

    """ Test case for web Exceptions with 200x status codes """

    def test_view(self):
        """ Check is base view without exception correct response"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), "Thist is default view response")

    @mock.patch('tests.views.IndexView.get', mock_view(
        exceptions.HTTPOk, content='exception 200 ok content', headers={'X-key': 'X-value'}))
    def test_200(self):
        """ Check is raised exception return correct HTTP Response with status 200 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), "exception 200 ok content")
        self.assertTrue(response.has_header('X-key'))

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPCreated))
    def test_201(self):
        """ Check is raised exception return correct HTTP Response with status 201 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content.decode('utf-8'), "201: Created")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPAccepted))
    def test_202(self):
        """ Check is raised exception return correct HTTP Response with status 202 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 202)
        self.assertEqual(response.content.decode('utf-8'), "202: Accepted")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPNonAuthoritativeInformation))
    def test_203(self):
        """ Check is raised exception return correct HTTP Response with status 203 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 203)
        self.assertEqual(response.content.decode('utf-8'), "203: Non-Authoritative Information")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPNoContent, headers={'X-key': 'X-value'}))
    def test_204(self):
        """ Check is raised exception return correct HTTP Response with status 204 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.content.decode('utf-8'), '')
        self.assertTrue(response.has_header('X-key'))

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPResetContent))
    def test_205(self):
        """ Check is raised exception return correct HTTP Response with status 205 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 205)
        self.assertEqual(response.content.decode('utf-8'), '')

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPPartialContent))
    def test_206(self):
        """ Check is raised exception return correct HTTP Response with status 206 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 206)
        self.assertEqual(response.content.decode('utf-8'), "206: Partial Content")


class TestWebExceptions300(TestCase):

    """ Test case for web Exceptions with 300x status codes """

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPMultipleChoices, location='/foo'))
    def test_300(self):
        """ Check is raised exception return correct HTTP Response with status 300 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 300)
        self.assertEqual(response.content.decode('utf-8'), '300: Multiple Choices')
        self.assertTrue(response.has_header('Location'))
        self.assertEqual(response.location, '/foo')

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPMovedPermanently, location='/foo'))
    def test_301(self):
        """ Check is raised exception return correct HTTP Response with status 301 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.content.decode('utf-8'), '301: Multiple Choices')
        self.assertTrue(response.has_header('Location'))
        self.assertEqual(response.location, '/foo')

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPFound, location='/foo'))
    def test_302(self):
        """ Check is raised exception return correct HTTP Response with status 302 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.content.decode('utf-8'), '302: Multiple Choices')
        self.assertTrue(response.has_header('Location'))
        self.assertEqual(response.location, '/foo')

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPSeeOther, location='/foo'))
    def test_303(self):
        """ Check is raised exception return correct HTTP Response with status 303 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 303)
        self.assertEqual(response.content.decode('utf-8'), '303: Multiple Choices')
        self.assertTrue(response.has_header('Location'))
        self.assertEqual(response.location, '/foo')

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPNotModified, location='/foo'))
    def test_304(self):
        """ Check is raised exception return correct HTTP Response with status 304 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 304)
        self.assertEqual(response.content.decode('utf-8'), '')
        self.assertTrue(response.has_header('Location'))
        self.assertEqual(response.location, '/foo')

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPUseProxy, location='/foo'))
    def test_305(self):
        """ Check is raised exception return correct HTTP Response with status 305 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 305)
        self.assertEqual(response.content.decode('utf-8'), '')
        self.assertTrue(response.has_header('Location'))
        self.assertEqual(response.location, '/foo')

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPTemporaryRedirect, location='/foo'))
    def test_306(self):
        """ Check is raised exception return correct HTTP Response with status 306 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 306)
        self.assertEqual(response.content.decode('utf-8'), '')
        self.assertTrue(response.has_header('Location'))
        self.assertEqual(response.location, '/foo')

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPPermanentRedirect, location='/foo'))
    def test_307(self):
        """ Check is raised exception return correct HTTP Response with status 307 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 307)
        self.assertEqual(response.content.decode('utf-8'), '')
        self.assertTrue(response.has_header('Location'))
        self.assertEqual(response.location, '/foo')

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPPermanentRedirect, location='/foo'))
    def test_308(self):
        """ Check is raised exception return correct HTTP Response with status 308 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 308)
        self.assertEqual(response.content.decode('utf-8'), '')
        self.assertTrue(response.has_header('Location'))
        self.assertEqual(response.location, '/foo')



#     # 300x status code
#     'HTTPNotModified',
#     '',
#     '',
#     '',
#     # 400x status code
#     'HTTPBadRequest',
#     'HTTPUnauthorized',
#     'HTTPPaymentRequired',
#     'HTTPForbidden',
#     'HTTPNotFound',
#     'HTTPMethodNotAllowed',
#     'HTTPNotAcceptable',
#     'HTTPProxyAuthenticationRequired',
#     'HTTPRequestTimeout',
#     'HTTPConflict',
#     'HTTPGone',
#     'HTTPLengthRequired',
#     'HTTPPreconditionFailed',
#     'HTTPRequestEntityTooLarge',
#     'HTTPRequestURITooLong',
#     'HTTPUnsupportedMediaType',
#     'HTTPRequestRangeNotSatisfiable',
#     'HTTPExpectationFailed',
#     'HTTPMisdirectedRequest',
#     'HTTPUpgradeRequired',
#     'HTTPPreconditionRequired',
#     'HTTPTooManyRequests',
#     'HTTPRequestHeaderFieldsTooLarge',
#     'HTTPUnavailableForLegalReasons',
#     # 500x status code
#     'HTTPInternalServerError',
#     'HTTPNotImplemented',
#     'HTTPBadGateway',
#     'HTTPServiceUnavailable',
#     'HTTPGatewayTimeout',
#     'HTTPVersionNotSupported',
#     'HTTPVariantAlsoNegotiates',
#     'HTTPNotExtended',
#     'HTTPNetworkAuthenticationRequired',
# )