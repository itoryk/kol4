from framework.types import RequestT
from framework.types import ResponseT
from framework.utils import read_static


def handle_logo(_request: RequestT) -> ResponseT:
    payload = read_static("123.jpg")
    status = "200 OK"
    headers = {"Content-type": "image/jpeg"}

    return ResponseT(status, headers, payload)
