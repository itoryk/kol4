import http
import mimetypes
import re
from html import escape
from pathlib import Path
from typing import Any
from typing import Callable
from typing import Tuple
from urllib.parse import parse_qs

from framework.consts import DIR_STATIC
from framework.errors import NotFound
from framework.types import StaticT


def http_first(value: Tuple[str, Any]) -> tuple:
    if value[0].startswith("HTTP"):
        return 0, value
    return 1, value


def format_env_var(name: str, value: str) -> str:
    formatter = get_formatter(name)
    new = str(value)
    new = formatter(new)
    new = escape(new)
    new = re.sub("\n", "<br>", new)

    return new


def get_formatter(env_var_name: str) -> Callable[[str], str]:
    if env_var_name.endswith("PATH"):
        return lambda _value: "\n".join(_value.split(":"))
    if "ACCEPT" in env_var_name:
        return lambda _v: "\n".join(re.split(r"[\s,]+", _v))
    return lambda _v: _v


def read_static(file_name: str) -> StaticT:
    if file_name.startswith("/"):
        file_obj = path(file_name).resolve()
    else:
        file_obj = (DIR_STATIC / file_name).resolve()

    if not file_obj.exists():
        raise NotFound

    with file_obj.open("rb") as fp:
        content = fp.read()

    content_type = mimetypes.guess_type(file_name)[0]

    return StaticT(content=content, content_type=content_type)


def get_request_headers(environ: dict) -> dict:
    environ_headers = filter(lambda _kv: _kv[0].startswith("HTTP_"), environ.items())
    request_headers = {key[5:]: value for key, value in environ_headers}
    return request_headers


def get_query(environ: dict) -> dict:
    qs = environ.get("QUERY_STRING")
    query = parse_qs(qs or "")
    return query


def build_status(code: int) -> str:
    status = http.HTTPStatus(code)
    reason = "".join(word.capitalize() for word in status.name.split("_"))

    text = f"{code} {reason}"
    return text
