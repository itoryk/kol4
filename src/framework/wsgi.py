from handlers import handle_index
from handlers import handle_logo
from handlers import handle_styles
from handlers import system_handlers
handlers = {"/": handle_index,
            "/styles.css": handle_styles,
            "/logo.jpeg": handle_logo
            }

def application(environ, start_response):

    url = environ["PATH_INFO"]
    status, headers, payload = handler(environ)
    start_response(status, list(headers.items()))

    yield payload

 
