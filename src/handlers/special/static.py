from framework.types import RequestT
from framework.types import ResponseT
from framework.util import build_status
from framework.util import read_static


def handle_static(request: RequestT) -> ResponseT:
    file_name = request.kwargs["file_name"]

    static = read_static(file_name)
    status = build_status(200)

    return ResponseT(
        headers={"Content-Type": static.content_type},
        payload=static.content,
        status=status,
    )
