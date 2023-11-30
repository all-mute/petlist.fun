from flet import (
    UserControl,
    Column,
    Row,
    Card,
    Icon,
    ResponsiveRow,
    Stack,
    OutlinedButton,
    LinearGradient,
    TextButton,
    FloatingActionButton,
    ElevatedButton,
    Text,
    MainAxisAlignment,
    GridView,
    Container,
    TextField,
    AlertDialog,
    Container,
    icons,
    border_radius,
    border,
    colors,
    padding,
    alignment,
    margin
)

from ..class_project import Project
from ..configuration.hashtags import get_hashtags_list_short
from .microcard import ProjectCard


class GridWithHashtags(UserControl):
    def __init__(
        self,
        projects: list[Project],
    ):
        super().__init__()
        self.projects = projects
        self.wrap_status = False

    def build(self):
        self.hashtags_button_down = \
            Container(
                content=Icon(name=icons.KEYBOARD_ARROW_DOWN, scale=1.24),
                bgcolor=colors.SURFACE,
                height=32,
                width=32,
                on_click=self.wrap_hashtags
            )

        self.hashtags_wrap_button_changing = [
            self.hashtags_button_down,
            #self.hashtags_button_down
        ]

        self.cards = [
            ProjectCard(
                project_name=project.name,
                hashtags=project.hashtags,
                number_of_likes=project.n_likes,
                liked=project.liked_by,
            )
            for project in self.projects
        ]

        # слой для hashtags
        self.hashtags_row = \
            Row(
                [
                    *[
                        OutlinedButton(
                            ht,
                            scale=0.85,
                        )
                        for ht in get_hashtags_list_short()
                    ],
                    # пространство сзади кнопки
                    Container(width=32)
                ],
                scroll="adaptive",
                col=2,
                spacing=0,
                run_spacing=0,
            )

        # слой для кнопки # слой для gradient & wrap-button
        self.hashtags_button_layer = \
            Row(
                [
                    # TODO change LinearGradient to ShaderMask https://flet.dev/docs/controls/shadermask/
                    Container(
                        gradient=LinearGradient(
                            begin=alignment.center_left,
                            end=alignment.center_right,
                            colors=[colors.TRANSPARENT, colors.SURFACE],
                        ),
                        width=32,
                    ),
                    # False = 0 = unwrapped
                    self.hashtags_wrap_button_changing[int(self.wrap_status)]
                ],
                alignment=MainAxisAlignment.END,
                run_spacing=0,
                spacing=0,
                height=32,
            )

        # container for hashtags
        self.hashtags_container = \
            Container(
                Stack(
                    [
                        self.hashtags_row,
                        self.hashtags_button_layer,
                    ]
                )
            )

        # TODO позже разбивать проекты по 12 штук и закидывать в оптимизированный ListView или GridView
        # container for cards
        self.cards_container = \
            Container(
                ResponsiveRow(
                    controls=self.cards,
                    spacing={"lg": 30, "sm": 30, "xs": 0},
                    run_spacing={"lg": 30, "sm": 30, "xs": 30},
                )
            )

        self.final_column = \
            Container(
                Column(
                    [
                        self.hashtags_container,
                        Row(height=15),
                        self.cards_container,
                    ],
                    spacing=0,
                )
            )

        return self.final_column

    async def wrap_hashtags(self, e):
        self.hashtags_row.wrap = not self.hashtags_row.wrap
        icns = [icons.KEYBOARD_ARROW_DOWN, icons.KEYBOARD_ARROW_UP]
        self.wrap_status = not self.wrap_status
        self.hashtags_button_down.content.name = icns[int(self.wrap_status)]
        await self.update_async()

