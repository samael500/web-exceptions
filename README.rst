=============================
Django Web Exceptions
=============================

.. image:: https://badge.fury.io/py/web-exceptions.svg
    :target: https://badge.fury.io/py/web-exceptions

.. image:: https://travis-ci.org/samael500/web-exceptions.svg?branch=master
    :target: https://travis-ci.org/samael500/web-exceptions

.. image:: https://codecov.io/gh/samael500/web-exceptions/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/samael500/web-exceptions

Throwing web exceptions like in AioHTTP

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
