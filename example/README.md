## Example Project for web_exceptions

This example is provided as a convenience feature to allow potential users to try the app straight from the app repo without having to create a django project.

It can also be used to develop the app in place.

To run this example, follow these instructions:

1. Navigate to the `example` directory
2. Install the requirements for the package:
		
		pip install -r requirements.txt
		
3. Run the server

		python manage.py runserver
		
4. Access from the browser at `http://127.0.0.1:8000`


## Example result

### location [`/`](http://127.0.0.1:8000/)

Raised `HTTPOk` exception with extra headers and custom content

```python
exceptions.HTTPOk(
    content="Thist is Http Ok response",
    headers={'X-Extra-Header': 'some value'})
```

```diff
$ curl -v  http://localhost:8000/
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 8000 (#0)
> GET / HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.52.1
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Date: Sun, 14 May 2017 14:41:13 GMT
< Server: WSGIServer/0.2 CPython/3.6.0a1
< X-Frame-Options: SAMEORIGIN
< Content-Length: 25
< Content-Type: text/html; charset=utf-8
< X-Extra-Header: some value
< 
* Curl_http_done: called premature == 0
* Closing connection 0
Thist is Http Ok response
```

### location [`/tea`](http://127.0.0.1:8000/tea)

Raised custom `HTTPTeapot` exception with reason `I'm a teapot`

```python
class HTTPTeapot(exceptions.HTTPClientError):
    status_code = 418

# ...

raise HTTPTeapot(reason="I'm a teapot")
```

```diff
$ curl -v  http://localhost:8000/tea
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 8000 (#0)
> GET /tea HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.52.1
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 418 I'm a teapot
< Date: Sun, 14 May 2017 14:47:31 GMT
< Server: WSGIServer/0.2 CPython/3.6.0a1
< X-Frame-Options: SAMEORIGIN
< Content-Length: 17
< Content-Type: text/html; charset=utf-8
< 
* Curl_http_done: called premature == 0
* Closing connection 0
418: I'm a teapot
```

### location [`/coffee`](http://127.0.0.1:8000/coffee)

301 Redirect to a `/tea` by raise `HTTPMovedPermanently`

```python
raise exceptions.HTTPMovedPermanently('/tea')
```

```diff
$ curl -vL  http://localhost:8000/coffee
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 8000 (#0)
> GET /coffee HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.52.1
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 301 Moved Permanently
< Date: Sun, 14 May 2017 14:49:17 GMT
< Server: WSGIServer/0.2 CPython/3.6.0a1
< X-Frame-Options: SAMEORIGIN
< Location: /tea
< Content-Type: text/html; charset=utf-8
< Content-Length: 22
< 
* Curl_http_done: called premature == 0
* Closing connection 0
* Issue another request to this URL: 'http://localhost:8000/tea'
* Hostname localhost was found in DNS cache
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 8000 (#1)
> GET /tea HTTP/1.0
> Host: localhost:8000
> User-Agent: curl/7.52.1
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 418 I'm a teapot
< Date: Sun, 14 May 2017 14:49:17 GMT
< Server: WSGIServer/0.2 CPython/3.6.0a1
< X-Frame-Options: SAMEORIGIN
< Content-Length: 17
< Content-Type: text/html; charset=utf-8
< 
* Curl_http_done: called premature == 0
* Closing connection 1
418: I'm a teapot
```

### location [`/timeout`](http://127.0.0.1:8000/timeout)

Raise `HTTPRequestTimeout` with `408` status code.
Response customized by define `handler408` in `urls.py`

```python
raise exceptions.HTTPRequestTimeout()

# ...

def handler408(request):
    """ Custom response handler """
    return HttpResponse(content="Custom 408 handler", status=408)
```

```diff
$ curl -v  http://localhost:8000/timeout
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 8000 (#0)
> GET /timeout HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.52.1
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 408 Request Timeout
< Date: Sun, 14 May 2017 14:53:02 GMT
< Server: WSGIServer/0.2 CPython/3.6.0a1
< X-Frame-Options: SAMEORIGIN
< Content-Length: 18
< Content-Type: text/html; charset=utf-8
< 
* Curl_http_done: called premature == 0
* Closing connection 0
Custom 408 handler
```
