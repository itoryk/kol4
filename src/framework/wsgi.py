import mimetypes

from framework.consts import DIR_STATIC


def application(environ, start_response):
    url = environ["PATH_INFO"]

    file_names = {
        "/styles.css": "styles.css",
        "/logo.jpeg": "123.jpg",
    }
    status = "200 OK"
    file_name = file_names.get(url, "payload.html")
    headers = {
        "Content-type": mimetypes.guess_type(file_name)[0],
    }
    payload = read_static(file_name)
    start_response(status, list(headers.items()))

    yield payload


def read_static(file_name: str) -> bytes:
    path = DIR_STATIC / file_name
    with path.open("rb") as fp:
        payload = fp.read()
    return payload
