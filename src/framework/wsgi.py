from framework.types import RequestT
from handlers import handle_index
from handlers import handle_logo
from handlers import handle_styles
from handlers import system_handlers

handlers = {"/": handle_index, "/styles.css": handle_styles, "/logo.jpeg": handle_logo}

def application(environ: dict, start_response):

    url = environ["PATH_INFO"]

    handler = handlers.get(url, system_handlers.handle_404)

    request_headers = {
        key[5:]: environ[key]
        for key in filter(lambda i: i.startswith("HTTP_"), environ)
    }

    request = RequestT(
        method=environ["REQUEST_METHOD"],
        path=url,
        headers=request_headers,
    )

    response = handler(request)

    start_response(response.status, list(response.headers.items()))

    yield response.payload
