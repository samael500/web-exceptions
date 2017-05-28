=====
Usage
=====

To use Django Web Exceptions in a project, add it to your `MIDDLEWARE` settings:

.. code-block:: python
    :caption: settings.py

    MIDDLEWARE = [
        ...
        # add middleware for dj exceptions
        'web_exceptions.middleware.WebExceptionsMiddleware',
        ...
    ]


Import and raise Web Exceptions's:

.. code-block:: python

    from web_exceptions import exceptions

    ...

    raise exceptions.HTTPOk(
        content="Thist is Http Ok response",
        headers={'X-Extra-Header': 'some value'})


Declare custom web exception:

.. code-block:: python

    from web_exceptions import exceptions


    class HTTPTeapot(exceptions.HTTPClientError):
        status_code = 418
        reason = "I'm a teapot"

    ...

    raise HTTPTeapot()


Also you can customize any kind of exception status code as custom handler,
defined in `urls.py` like `django error handlers`_ .


.. code-block:: python
    :caption: urls.py

    from myapp import views

    handler300 = <callable view>
    handler400 = <callable view>
    handler<status_code> = <callable view>


.. _django error handlers: https://docs.djangoproject.com/en/1.11/topics/http/views/#customizing-error-views
