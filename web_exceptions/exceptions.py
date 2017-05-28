from django.http import HttpResponse

__all__ = (
    # base exceptions
    'HTTPException',
    'HTTPError',
    'HTTPRedirection',
    'HTTPSuccessful',
    'HTTPClientError',
    'HTTPServerError',
    # 200x status code
    'HTTPOk',
    'HTTPCreated',
    'HTTPAccepted',
    'HTTPNonAuthoritativeInformation',
    'HTTPNoContent',
    'HTTPResetContent',
    'HTTPPartialContent',
    # 300x status code
    'HTTPMultipleChoices',
    'HTTPMovedPermanently',
    'HTTPFound',
    'HTTPSeeOther',
    'HTTPNotModified',
    'HTTPUseProxy',
    'HTTPTemporaryRedirect',
    'HTTPPermanentRedirect',
    # 400x status code
    'HTTPBadRequest',
    'HTTPUnauthorized',
    'HTTPPaymentRequired',
    'HTTPForbidden',
    'HTTPNotFound',
    'HTTPMethodNotAllowed',
    'HTTPNotAcceptable',
    'HTTPProxyAuthenticationRequired',
    'HTTPRequestTimeout',
    'HTTPConflict',
    'HTTPGone',
    'HTTPLengthRequired',
    'HTTPPreconditionFailed',
    'HTTPRequestEntityTooLarge',
    'HTTPRequestURITooLong',
    'HTTPUnsupportedMediaType',
    'HTTPRequestRangeNotSatisfiable',
    'HTTPExpectationFailed',
    'HTTPMisdirectedRequest',
    'HTTPUpgradeRequired',
    'HTTPPreconditionRequired',
    'HTTPTooManyRequests',
    'HTTPRequestHeaderFieldsTooLarge',
    'HTTPUnavailableForLegalReasons',
    # 500x status code
    'HTTPInternalServerError',
    'HTTPNotImplemented',
    'HTTPBadGateway',
    'HTTPServiceUnavailable',
    'HTTPGatewayTimeout',
    'HTTPVersionNotSupported',
    'HTTPVariantAlsoNegotiates',
    'HTTPNotExtended',
    'HTTPNetworkAuthenticationRequired',
)


class HTTPException(HttpResponse, Exception):

    """
    Base Web explanation
    In subclasses should set status_code attr
    """

    status_code = None
    empty_body = False
    reason = None

    def __init__(self, *, content=None, headers=None, **kwargs):
        HttpResponse.__init__(self, content or "", status=self.status_code, **kwargs)
        headers = headers or {}
        for key, value in headers.items():
            self[key] = value
        self._reason_phrase = self._reason_phrase or self.reason
        if not (self.content or self.empty_body):
            self.content = "{}: {}".format(self.status_code, self.reason_phrase).encode(self.charset)
        Exception.__init__(self, self.reason_phrase)


class HTTPError(HTTPException):

    """ Base class for exceptions with status codes in the 400s and 500s. """


class HTTPRedirection(HTTPException):

    """ Base class for exceptions with status codes in the 300s. """


class HTTPSuccessful(HTTPException):

    """ Base class for exceptions with status codes in the 200s. """


class HTTPClientError(HTTPError):

    """ Base class for exceptions with status codes in the 400s. """


class HTTPServerError(HTTPError):

    """ Base class for exceptions with status codes in the 500s. """


class HTTPOk(HTTPSuccessful):
    status_code = 200


class HTTPCreated(HTTPSuccessful):
    status_code = 201


class HTTPAccepted(HTTPSuccessful):
    status_code = 202


class HTTPNonAuthoritativeInformation(HTTPSuccessful):
    status_code = 203


class HTTPNoContent(HTTPSuccessful):
    status_code = 204
    empty_body = True


class HTTPResetContent(HTTPSuccessful):
    status_code = 205
    empty_body = True


class HTTPPartialContent(HTTPSuccessful):
    status_code = 206


class _HTTPMove(HTTPRedirection):

    def __init__(self, location, **kwargs):
        if not location:
            raise ValueError("HTTP redirects need a location to redirect to.")
        super().__init__(**kwargs)
        self['Location'] = str(location)
        self.location = location


class HTTPMultipleChoices(_HTTPMove):
    status_code = 300


class HTTPMovedPermanently(_HTTPMove):
    status_code = 301


class HTTPFound(_HTTPMove):
    status_code = 302


class HTTPSeeOther(_HTTPMove):
    status_code = 303


class HTTPNotModified(HTTPRedirection):
    status_code = 304
    empty_body = True


class HTTPUseProxy(_HTTPMove):
    status_code = 305


class HTTPTemporaryRedirect(_HTTPMove):
    status_code = 307


class HTTPPermanentRedirect(_HTTPMove):
    status_code = 308
    reason = "Permanent Redirect"


class HTTPBadRequest(HTTPClientError):
    status_code = 400


class HTTPUnauthorized(HTTPClientError):
    status_code = 401


class HTTPPaymentRequired(HTTPClientError):
    status_code = 402


class HTTPForbidden(HTTPClientError):
    status_code = 403


class HTTPNotFound(HTTPClientError):
    status_code = 404


class HTTPMethodNotAllowed(HTTPClientError):
    status_code = 405

    def __init__(self, method, allowed_methods, **kwargs):
        allow = ','.join(sorted(allowed_methods)).upper()
        super().__init__(**kwargs)
        self['Allow'] = allow
        self.allowed_methods = allowed_methods
        self.method = method.upper()


class HTTPNotAcceptable(HTTPClientError):
    status_code = 406


class HTTPProxyAuthenticationRequired(HTTPClientError):
    status_code = 407


class HTTPRequestTimeout(HTTPClientError):
    status_code = 408


class HTTPConflict(HTTPClientError):
    status_code = 409


class HTTPGone(HTTPClientError):
    status_code = 410


class HTTPLengthRequired(HTTPClientError):
    status_code = 411


class HTTPPreconditionFailed(HTTPClientError):
    status_code = 412


class HTTPRequestEntityTooLarge(HTTPClientError):
    status_code = 413


class HTTPRequestURITooLong(HTTPClientError):
    status_code = 414


class HTTPUnsupportedMediaType(HTTPClientError):
    status_code = 415


class HTTPRequestRangeNotSatisfiable(HTTPClientError):
    status_code = 416


class HTTPExpectationFailed(HTTPClientError):
    status_code = 417


class HTTPMisdirectedRequest(HTTPClientError):
    status_code = 421
    reason = "Misdirected Request"


class HTTPUpgradeRequired(HTTPClientError):
    status_code = 426
    reason = "Upgrade Required"


class HTTPPreconditionRequired(HTTPClientError):
    status_code = 428


class HTTPTooManyRequests(HTTPClientError):
    status_code = 429


class HTTPRequestHeaderFieldsTooLarge(HTTPClientError):
    status_code = 431


class HTTPUnavailableForLegalReasons(HTTPClientError):
    status_code = 451
    reason = "Unavailable for legal reasons"

    def __init__(self, link, **kwargs):
        super().__init__(**kwargs)
        self['Link'] = '<{}>; rel="blocked-by"'.format(link)
        self.link = link


class HTTPInternalServerError(HTTPServerError):
    status_code = 500


class HTTPNotImplemented(HTTPServerError):
    status_code = 501


class HTTPBadGateway(HTTPServerError):
    status_code = 502


class HTTPServiceUnavailable(HTTPServerError):
    status_code = 503


class HTTPGatewayTimeout(HTTPServerError):
    status_code = 504


class HTTPVersionNotSupported(HTTPServerError):
    status_code = 505


class HTTPVariantAlsoNegotiates(HTTPServerError):
    status_code = 506
    reason = "Variant Also Negotiates"


class HTTPNotExtended(HTTPServerError):
    status_code = 510
    reason = "Not Extended"


class HTTPNetworkAuthenticationRequired(HTTPServerError):
    status_code = 511
