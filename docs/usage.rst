=====
Usage
=====

Configure
---------

To use Django Web Exceptions in a project, add it to your `MIDDLEWARE` settings:

.. code-block:: python

    # settings.py
    MIDDLEWARE = [
        ...
        # add middleware for dj exceptions
        'web_exceptions.middleware.WebExceptionsMiddleware',
        ...
    ]

Simple usage
------------

Import and raise Web Exceptions's:

.. code-block:: python

    from web_exceptions import exceptions

    ...

    raise exceptions.HTTPOk(
        content="Thist is Http Ok response",
        headers={'X-Extra-Header': 'some value'})


Customize response
------------------

Self http exception
~~~~~~~~~~~~~~~~~~~

Declare custom web exception:

.. code-block:: python

    from web_exceptions import exceptions


    class HTTPTeapot(exceptions.HTTPClientError):
        status_code = 418
        reason = "I'm a teapot"

    ...

    raise HTTPTeapot()

Self response handler
~~~~~~~~~~~~~~~~~~~~~

Also you can customize any kind of exception status code as custom handler,
defined in `urls.py` like `django error handlers`_.


.. code-block:: python

    # urls.py
    from myapp import views

    handler300 = <callable view>
    handler400 = <callable view>
    handler<status_code> = <callable view>


.. _django error handlers: https://docs.djangoproject.com/en/1.11/topics/http/views/#customizing-error-views


List of available exceptions
----------------------------

200x status code
~~~~~~~~~~~~~~~~

- `200` HTTPOk
- `201` HTTPCreated
- `202` HTTPAccepted
- `203` HTTPNonAuthoritativeInformation
- `204` HTTPNoContent
- `205` HTTPResetContent
- `206` HTTPPartialContent

300x status code
~~~~~~~~~~~~~~~~

- `300` HTTPMultipleChoices
- `301` HTTPMovedPermanently
- `302` HTTPFound
- `303` HTTPSeeOther
- `304` HTTPNotModified
- `305` HTTPUseProxy
- `307` HTTPTemporaryRedirect
- `308` HTTPPermanentRedirect

400x status code
~~~~~~~~~~~~~~~~

- `400` HTTPBadRequest
- `401` HTTPUnauthorized
- `402` HTTPPaymentRequired
- `403` HTTPForbidden
- `404` HTTPNotFound
- `405` HTTPMethodNotAllowed
- `406` HTTPNotAcceptable
- `407` HTTPProxyAuthenticationRequired
- `408` HTTPRequestTimeout
- `409` HTTPConflict
- `410` HTTPGone
- `411` HTTPLengthRequired
- `412` HTTPPreconditionFailed
- `413` HTTPRequestEntityTooLarge
- `414` HTTPRequestURITooLong
- `415` HTTPUnsupportedMediaType
- `416` HTTPRequestRangeNotSatisfiable
- `417` HTTPExpectationFailed
- `421` HTTPMisdirectedRequest
- `426` HTTPUpgradeRequired
- `428` HTTPPreconditionRequired
- `429` HTTPTooManyRequests
- `431` HTTPRequestHeaderFieldsTooLarge
- `451` HTTPUnavailableForLegalReasons

500x status code
~~~~~~~~~~~~~~~~

- `500` HTTPInternalServerError
- `501` HTTPNotImplemented
- `502` HTTPBadGateway
- `503` HTTPServiceUnavailable
- `504` HTTPGatewayTimeout
- `505` HTTPVersionNotSupported
- `506` HTTPVariantAlsoNegotiates
- `510` HTTPNotExtended
- `511` HTTPNetworkAuthenticationRequired
