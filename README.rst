=============================
Django Web Exceptions
=============================

.. image:: https://badge.fury.io/py/django-web-exceptions.svg
    :target: https://badge.fury.io/py/django-web-exceptions

.. image:: https://travis-ci.org/samael500/web-exceptions.svg?branch=master
    :target: https://travis-ci.org/samael500/web-exceptions

.. image:: https://codecov.io/gh/samael500/web-exceptions/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/samael500/web-exceptions

Throwing web exceptions like in AioHTTP

What and why?
-------------

In AioHTTP_ you cat raise any response as exception (this is very cool).
But Django can raise only 3+1 web exceptions.

- `400` `SuspiciousOperation <https://docs.djangoproject.com/en/1.11/ref/exceptions/#suspiciousoperation>`_
- `403` `PermissionDenied <https://docs.djangoproject.com/en/1.11/ref/exceptions/#permissiondenied>`_
- `404` `Http404 <https://docs.djangoproject.com/en/1.11/topics/http/views/#the-http404-exception>`_
- `500` Any other non catched exception

This package allow you to raise as exception any on HTTP response.

.. And configure any custome `handlerXXX` for that.

.. Documentation
.. -------------

.. The full documentation is at https://web-exceptions.readthedocs.io.

Quickstart
----------

Install Django Web Exceptions::

    pip install django-web-exceptions

Add it to your `MIDDLEWARE`:

.. code-block:: python

    MIDDLEWARE = (
        # ...
        'web_exceptions.middleware.WebExceptionsMiddleware',
        # ...
    )

Features
--------

Import exceptions and raise anywhere

.. code-block:: python

    from web_exceptions import exceptions

    # ...

    def index(request):
        """ Simple view raise redirectexception """
        raise exceptions.HTTPMovedPermanently('/foo')


Also you cat customize any kind of exception status code as custom handler,
defined in `urls.py` like `django error handlers <https://docs.djangoproject.com/en/1.11/topics/http/views/#customizing-error-views>`_ .

.. code-block:: python

    # urls.py

    from myapp import views

    handler300 = <callable view>
    handler400 = <callable view>
    handler<status_code> = <callable view>


Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
.. _AioHTTP: https://github.com/aio-libs/aiohttp
