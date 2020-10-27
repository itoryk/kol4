import random
from mimetypes import guess_type

from framework.consts import DIR_STATIC


def application(environ, start_response):
    url = environ["PATH_INFO"]
    handlers = {"/": handler_index}
    handler = handlers.get(url, handler_404)
    status = "200 OK"
    headers = {
        "Content-type": "text/html",
    }
    payload = handler(environ)
    start_response(status, list(headers.items()))

    yield payload


def read_static(file_name: str) -> bytes:
    path = DIR_STATIC / file_name
    with path.open("rb") as fp:
        payload = fp.read()
    return payload


def handler_index(_environ) -> bytes:
    handler_html = read_static("handler.html").decode()
    payload_html = read_static("payload.html").decode()
    text = handler_html.format(xxx=payload_html)
    return text.encode()


def handler_404(environ) -> bytes:
    url = environ["PATH_INFO"]
    pin = random.randint(1, 1000)
    msg = f"Hello world! Your path: {url} not found. Pin: {pin}"

    return msg.encode()
