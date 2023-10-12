from flet import (
    AlertDialog,
    AppBar,
    Column,
    Container,
    ElevatedButton,
    Icon,
    Page,
    PopupMenuButton,
    PopupMenuItem,
    RoundedRectangleBorder,
    Row,
    TemplateRoute,
    Text,
    TextField,
    UserControl,
    View,
    colors,
    icons,
    margin,
    padding,
    theme,
)

from .class_project import default_project, default_project2
from .custom_controls.cardsgrid import GridWithHashtags
from .custom_controls.staticappbar import StaticAppBar


class MainApp(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        #self.page.on_route_change = self.route_change
        #self.boards = self.store.get_boards()
        #self.page.update()

    def build(self):
        self.layout = Column(
            [
                StaticAppBar(),
                GridWithHashtags([default_project, default_project2] * 33),
            ],
            width=1142,
            spacing=0,
        )

        return self.layout
