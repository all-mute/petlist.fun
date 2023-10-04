from flet import (
    UserControl,
    Column,
    Row,
    Card,
    TextButton,
    FloatingActionButton,
    ElevatedButton,
    OutlinedButton,
    Text,
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


class StaticAppBar(UserControl):
    def __init__(
        self,
    ):
        super().__init__()

    def build(self):

        # container for add button
        self.container_for_add = \
            Container(
                OutlinedButton(
                    icon="add",
                    # TODO
                    #on_click=None,
                )
            )

        # Pet[].fun
        self.site_name = Text(value="Pet[].fun", style="headlineMedium", font_family="RobotoMono")

        # container for user avatar circle
        self.container_for_user_avatar_circle = \
            Container(
                content=CircleAvatar(
                    foreground_image_url="https://avatars.githubusercontent.com/u/25614260?v=4",
                    content=Text("NaN"),
                ),
                padding=10,

            )

        self.bar = Row(

            [
                self.container_for_add,
                self.site_name,
                self.container_for_user_avatar_circle,
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN,
        )

        self.bar_with_divider = Column(
            [
                self.bar,
                Divider(height=10),
            ]
        )

        return self.bar_with_divider
