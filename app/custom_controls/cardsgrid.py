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

    def build(self):
        self.cards = [
            ProjectCard(
                project_name=project.title,
                hashtags=project.tags,
                number_of_likes=project.likes,
                liked=project.liked_by_user
            )
            for project in self.projects
        ]

        #
        # container for hashtags
        self.hashtags_container = \
            Container(
                Stack(
                    [
                        # слой для hashtags
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
                        ),

                        # слой для gradient & wrap-button
                        Row(
                            [
                                Container(
                                    gradient=LinearGradient(
                                        begin=alignment.center_left,
                                        end=alignment.center_right,
                                        colors=[colors.TRANSPARENT, colors.SURFACE],
                                    ),
                                    width=32,
                                ),
                                Container(
                                    content=Icon(icons.KEYBOARD_ARROW_DOWN, scale=1.24),
                                    bgcolor=colors.SURFACE,
                                    height=32,
                                    width=32,
                                    # TODO wrap_tags
                                    #on_click=self.wrap_tags
                                )
                            ],
                            alignment=MainAxisAlignment.END,
                            run_spacing=0,
                            spacing=0,
                            height=32,
                        )
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
                        self.cards_container
                    ]
                )
            )

        return self.final_column
