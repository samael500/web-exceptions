=====
Usage
=====

To use Django Web Exceptions in a project, add it to your `INSTALLED_APPS`:

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
