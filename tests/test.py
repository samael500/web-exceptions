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

    @mock.patch('tests.views.IndexView.get', mock_view(RuntimeError, 'x test text'))
    def test_non_web_exception(self):
        """ Not web exception check (should error raised) """
        with self.assertRaises(RuntimeError) as err:
            response = self.client.get('/')
        self.assertEqual(str(err.exception), 'x test text')

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
        self.assertEqual(response.content.decode('utf-8'), '301: Moved Permanently')
        self.assertTrue(response.has_header('Location'))
        self.assertEqual(response.location, '/foo')

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPFound, location='/foo'))
    def test_302(self):
        """ Check is raised exception return correct HTTP Response with status 302 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.content.decode('utf-8'), '302: Found')
        self.assertTrue(response.has_header('Location'))
        self.assertEqual(response.location, '/foo')

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPSeeOther, location='/foo'))
    def test_303(self):
        """ Check is raised exception return correct HTTP Response with status 303 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 303)
        self.assertEqual(response.content.decode('utf-8'), '303: See Other')
        self.assertTrue(response.has_header('Location'))
        self.assertEqual(response.location, '/foo')

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPNotModified))
    def test_304(self):
        """ Check is raised exception return correct HTTP Response with status 304 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 304)
        self.assertEqual(response.content.decode('utf-8'), '')

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPUseProxy, location='/foo'))
    def test_305(self):
        """ Check is raised exception return correct HTTP Response with status 305 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 305)
        self.assertEqual(response.content.decode('utf-8'), '305: Use Proxy')
        self.assertTrue(response.has_header('Location'))
        self.assertEqual(response.location, '/foo')

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPTemporaryRedirect, location='/foo'))
    def test_307(self):
        """ Check is raised exception return correct HTTP Response with status 307 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 307)
        self.assertEqual(response.content.decode('utf-8'), '307: Temporary Redirect')
        self.assertTrue(response.has_header('Location'))
        self.assertEqual(response.location, '/foo')

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPPermanentRedirect, location='/foo'))
    def test_308(self):
        """ Check is raised exception return correct HTTP Response with status 308 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 308)
        self.assertEqual(response.content.decode('utf-8'), '308: Permanent Redirect')
        self.assertTrue(response.has_header('Location'))
        self.assertEqual(response.location, '/foo')


class TestWebExceptions400(TestCase):

    """ Test case for web Exceptions with 400x status codes """

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPBadRequest))
    def test_400(self):
        """ Check is raised exception return correct HTTP Response with status 400 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content.decode('utf-8'), "400: Bad Request")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPUnauthorized))
    def test_401(self):
        """ Check is raised exception return correct HTTP Response with status 401 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.content.decode('utf-8'), "401: Unauthorized")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPPaymentRequired))
    def test_402(self):
        """ Check is raised exception return correct HTTP Response with status 402 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 402)
        self.assertEqual(response.content.decode('utf-8'), "402: Payment Required")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPForbidden))
    def test_403(self):
        """ Check is raised exception return correct HTTP Response with status 403 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.content.decode('utf-8'), "403: Forbidden")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPNotFound))
    def test_404(self):
        """ Check is raised exception return correct HTTP Response with status 404 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content.decode('utf-8'), "404: Not Found")

    @mock.patch('tests.views.IndexView.get', mock_view(
        exceptions.HTTPMethodNotAllowed, method='POST', allowed_methods=['GET', 'HEAD', 'PUT', 'XXX']))
    def test_405(self):
        """ Check is raised exception return correct HTTP Response with status 405 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.content.decode('utf-8'), "405: Method Not Allowed")
        self.assertTrue(response.has_header('Allow'))
        self.assertEqual(response.method, 'POST')
        self.assertEqual(response.allowed_methods, ['GET', 'HEAD', 'PUT', 'XXX'])

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPNotAcceptable))
    def test_406(self):
        """ Check is raised exception return correct HTTP Response with status 406 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 406)
        self.assertEqual(response.content.decode('utf-8'), "406: Not Acceptable")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPProxyAuthenticationRequired))
    def test_407(self):
        """ Check is raised exception return correct HTTP Response with status 407 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 407)
        self.assertEqual(response.content.decode('utf-8'), "407: Proxy Authentication Required")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPRequestTimeout))
    def test_408(self):
        """ Check is raised exception return correct HTTP Response with status 408 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 408)
        self.assertEqual(response.content.decode('utf-8'), "408: Request Timeout")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPConflict))
    def test_409(self):
        """ Check is raised exception return correct HTTP Response with status 409 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.content.decode('utf-8'), "409: Conflict")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPGone))
    def test_410(self):
        """ Check is raised exception return correct HTTP Response with status 410 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 410)
        self.assertEqual(response.content.decode('utf-8'), "410: Gone")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPLengthRequired))
    def test_411(self):
        """ Check is raised exception return correct HTTP Response with status 411 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 411)
        self.assertEqual(response.content.decode('utf-8'), "411: Length Required")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPPreconditionFailed))
    def test_412(self):
        """ Check is raised exception return correct HTTP Response with status 412 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 412)
        self.assertEqual(response.content.decode('utf-8'), "412: Precondition Failed")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPRequestEntityTooLarge))
    def test_413(self):
        """ Check is raised exception return correct HTTP Response with status 413 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 413)
        self.assertEqual(response.content.decode('utf-8'), "413: Request Entity Too Large")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPRequestURITooLong))
    def test_414(self):
        """ Check is raised exception return correct HTTP Response with status 414 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 414)
        self.assertEqual(response.content.decode('utf-8'), "414: Request-URI Too Long")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPUnsupportedMediaType))
    def test_415(self):
        """ Check is raised exception return correct HTTP Response with status 415 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 415)
        self.assertEqual(response.content.decode('utf-8'), "415: Unsupported Media Type")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPRequestRangeNotSatisfiable))
    def test_416(self):
        """ Check is raised exception return correct HTTP Response with status 416 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 416)
        self.assertEqual(response.content.decode('utf-8'), "416: Requested Range Not Satisfiable")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPExpectationFailed))
    def test_417(self):
        """ Check is raised exception return correct HTTP Response with status 417 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 417)
        self.assertEqual(response.content.decode('utf-8'), "417: Expectation Failed")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPMisdirectedRequest))
    def test_421(self):
        """ Check is raised exception return correct HTTP Response with status 421 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 421)
        self.assertEqual(response.content.decode('utf-8'), "421: Unknown Status Code")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPUpgradeRequired))
    def test_426(self):
        """ Check is raised exception return correct HTTP Response with status 426 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 426)
        self.assertEqual(response.content.decode('utf-8'), "426: Upgrade Required")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPPreconditionRequired))
    def test_428(self):
        """ Check is raised exception return correct HTTP Response with status 428 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 428)
        self.assertEqual(response.content.decode('utf-8'), "428: Precondition Required")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPTooManyRequests))
    def test_429(self):
        """ Check is raised exception return correct HTTP Response with status 429 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 429)
        self.assertEqual(response.content.decode('utf-8'), "429: Too Many Requests")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPRequestHeaderFieldsTooLarge))
    def test_431(self):
        """ Check is raised exception return correct HTTP Response with status 431 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 431)
        self.assertEqual(response.content.decode('utf-8'), "431: Request Header Fields Too Large")

    @mock.patch('tests.views.IndexView.get', mock_view(
        exceptions.HTTPUnavailableForLegalReasons, link='/foo/boo/koo'))
    def test_451(self):
        """ Check is raised exception return correct HTTP Response with status 451 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 451)
        self.assertEqual(response.content.decode('utf-8'), "451: Unknown Status Code")
        self.assertTrue(response.has_header('Link'))
        self.assertEqual(response.link, '/foo/boo/koo')


class TestWebExceptions500(TestCase):

    """ Test case for web Exceptions with 500x status codes """

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPInternalServerError))
    def test_500(self):
        """ Check is raised exception return correct HTTP Response with status 500 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.content.decode('utf-8'), "500: Internal Server Error")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPNotImplemented))
    def test_501(self):
        """ Check is raised exception return correct HTTP Response with status 501 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 501)
        self.assertEqual(response.content.decode('utf-8'), "501: Not Implemented")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPBadGateway))
    def test_502(self):
        """ Check is raised exception return correct HTTP Response with status 502 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 502)
        self.assertEqual(response.content.decode('utf-8'), "502: Bad Gateway")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPServiceUnavailable))
    def test_503(self):
        """ Check is raised exception return correct HTTP Response with status 503 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 503)
        self.assertEqual(response.content.decode('utf-8'), "503: Service Unavailable")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPGatewayTimeout))
    def test_504(self):
        """ Check is raised exception return correct HTTP Response with status 504 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 504)
        self.assertEqual(response.content.decode('utf-8'), "504: Gateway Timeout")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPVersionNotSupported))
    def test_505(self):
        """ Check is raised exception return correct HTTP Response with status 505 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 505)
        self.assertEqual(response.content.decode('utf-8'), "505: HTTP Version Not Supported")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPVariantAlsoNegotiates))
    def test_506(self):
        """ Check is raised exception return correct HTTP Response with status 506 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 506)
        self.assertEqual(response.content.decode('utf-8'), "506: Variant Also Negotiates")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPNotExtended))
    def test_510(self):
        """ Check is raised exception return correct HTTP Response with status 510 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 510)
        self.assertEqual(response.content.decode('utf-8'), "510: Not Extended")

    @mock.patch('tests.views.IndexView.get', mock_view(exceptions.HTTPNetworkAuthenticationRequired))
    def test_511(self):
        """ Check is raised exception return correct HTTP Response with status 511 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 511)
        self.assertEqual(response.content.decode('utf-8'), "511: Network Authentication Required")


class TestWebExceptionsCustomHandler(TestCase):

    """ Test case for web Exceptions with custom handlers """

    class HTTP444(exceptions.HTTPClientError):
        status_code = 444

    @mock.patch('tests.views.IndexView.get', mock_view(HTTP444))
    def test_view(self):
        """ Check is custom handler response return """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 444)
        self.assertEqual(response.content.decode('utf-8'), "This is custom error handler")
