=====
Usage
=====

To use Django Web Exceptions in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'web_exceptions.apps.DjExceptionsConfig',
        ...
    )

Add Django Web Exceptions's URL patterns:

.. code-block:: python

    from web_exceptions import urls as web_exceptions_urls


    urlpatterns = [
        ...
        url(r'^', include(web_exceptions_urls)),
        ...
    ]
