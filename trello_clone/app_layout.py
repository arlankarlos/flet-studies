from flet import Column, Row, Container, Control, Page  # noqa: F401
from flet import Text, colors, icons, IconButton  # noqa: F401
from sidebar import Sidebar  # noqa: F401

class AppLayout(Row):
    def __init__(self, app, page: Page, *args, **kwargs):
        super().__init__(*args, **kwargs)