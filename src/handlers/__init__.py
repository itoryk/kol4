from framework.types import RequestT
from framework.types import ResponseT

from . import system_handlers
from .index import handle_index
from .logo import handle_logo
from .styles import handle_styles


def handle_hello():
    return None
