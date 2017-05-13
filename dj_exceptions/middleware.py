from dj_exceptions.exceptions import HTTPException


class WebExceptionsMiddleware(object):

    def process_exception(self, request, exception):
        if isinstance(exception, HTTPException):
            return exception
