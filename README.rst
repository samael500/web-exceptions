=============================
Django Web Exceptions
=============================

.. image:: https://badge.fury.io/py/dj-exceptions.svg
    :target: https://badge.fury.io/py/dj-exceptions

.. image:: https://travis-ci.org/samael500/dj-exceptions.svg?branch=master
    :target: https://travis-ci.org/samael500/dj-exceptions

.. image:: https://codecov.io/gh/samael500/dj-exceptions/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/samael500/dj-exceptions

Throwing web exceptions like in AioHTTP

Documentation
-------------

The full documentation is at https://dj-exceptions.readthedocs.io.

Quickstart
----------

Install Django Web Exceptions::

    pip install dj-exceptions

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_exceptions.apps.DjExceptionsConfig',
        ...
    )

Add Django Web Exceptions's URL patterns:

.. code-block:: python

    from dj_exceptions import urls as dj_exceptions_urls


    urlpatterns = [
        ...
        url(r'^', include(dj_exceptions_urls)),
        ...
    ]

Features
--------

* TODO

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
