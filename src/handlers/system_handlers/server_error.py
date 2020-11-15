import traceback

from framework.types import RequestT
from framework.types import ResponseT


def handle_500(request: RequestT = None) -> ResponseT:
    document = traceback.format_exe()
    status = "500 Internal Server Error"
    headers = {"Content-type": "text/html"}
    payload = document.encode()

    return ResponseT(status, headers, payload)
