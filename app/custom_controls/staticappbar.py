from flet import (
    UserControl,
    Column,
    Row,
    Card,
    TextButton,
    IconButton,
    PopupMenuButton,
    PopupMenuItem,
    FloatingActionButton,
    ElevatedButton,
    OutlinedButton,
    Text,
    Icon,
    CircleAvatar,
    MainAxisAlignment,
    GridView,
    Container,
    TextField,
    AlertDialog,
    Container,
    Divider,
    icons,
    border_radius,
    border,
    colors,
    padding,
    alignment,
    margin
)

from .my_beautifull_add_button import AddOutlinedIconButton


class StaticAppBar(UserControl):
    def __init__(
        self,
    ):
        super().__init__()

    def build(self):

        # container for add button 0
        self.container_for_add = AddOutlinedIconButton()

        # container for add button 1
        self.container_for_add = \
            Container(
                OutlinedButton(
                    content=Icon("add"),
                )
            )

        # container for add button 2
        self.container_for_add = \
            Container(
                IconButton(
                    icon="add",
                    icon_size=32,
                    #icon_color=colors.PRIMARY,
                ),
                #margin=margin.only(left=10),
            )

        # Pet[].fun
        self.site_name = Text(value="Pet[].fun", size=28, font_family="RobotoMono")

        # container for user avatar circle
        self.container_for_user_avatar_circle = \
            Container(
                content=CircleAvatar(
                    foreground_image_url="https://avatars.githubusercontent.com/u/25614260?v=4",
                    content=Text("NaN"),
                    scale=1,
                ),
                padding=0,

            )

        self.popup_items = [
            PopupMenuItem(
                text="Login via Google",
            ),
            PopupMenuItem(
                text="Login via GitHub",
            ),
            PopupMenuItem(
                text="Log out",
            ),
            PopupMenuItem(),
            PopupMenuItem(
                text="Change theme",
            ),
            PopupMenuItem(
                text="About",
            )
        ]

        # TODO themes
        self.popup_menu_button = \
            Container(
                PopupMenuButton(
                    content=self.container_for_user_avatar_circle,
                    items=self.popup_items,
                ),
                padding=padding.only(right=10)
            )

        self.container_for_right_buttons = \
            Container(
                Row(
                    [
                        self.popup_menu_button,
                    ],
                    spacing=0,
                )
            )

        self.bar = Container(
            Row(

                [
                    self.container_for_add,
                    self.site_name,
                    self.container_for_right_buttons,
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN,

            ),
            # 20, 10
            margin=margin.only(left=0, right=0, top=20, bottom=20),
        )

        self.bar_with_divider = Column(
            [
                self.bar,
                Divider(height=2),
                Row(height=20)
            ],
            spacing=0,
        )

        return self.bar_with_divider
