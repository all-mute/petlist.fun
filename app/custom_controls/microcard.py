from flet import (
    UserControl,
    Column,
    Row,
    Card,
    TextButton,
    FloatingActionButton,
    ElevatedButton,
    Text,
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


class ProjectCard(UserControl):
    def __init__(
        self,
        project_name: str,
        hashtags: list,
        number_of_likes: int,
        liked: bool = False
    ):
        super().__init__()
        self.project_name = project_name
        self.hashtags = hashtags
        self.number_of_likes = number_of_likes
        self.liked = liked
        self.col = {"lg": 4, "sm": 6, "xs": 12}

    def build(self):
        # container for project name
        self.container_for_project_name = \
            Container(
                Text(
                    self.project_name,
                    size=20,
                    font_family="RobotoMono",
                    selectable=True,
                ),
                padding=padding.only(0, 0, 0, 20),
            )

        # container for hashtags
        self.container_for_hashtags = \
            Container(
                Row(
                    [
                        Text(
                            ht_name,
                            # TODO font_family
                            font_family=None,
                        )
                        for ht_name in self.hashtags
                    ],
                    spacing=10,
                    run_spacing=0,
                    scroll="adaptive",
                ),
                padding=padding.only(0, 0, 0, 0),
            )

        # container for likes
        self.container_for_likes = \
            Container(
                TextButton(
                    #text=(str(self.number_of_likes + int(self.liked)) + " 🔥"),
                    text=(str(4) + " 🔥"),
                    on_click=self.like_project,
                )
            )

        self.card = \
            Container(
                Card(
                    Container(
                        Column(
                            [
                                self.container_for_project_name,
                                self.container_for_hashtags,
                                self.container_for_likes
                            ]
                        ),
                        padding=padding.only(20, 30, 20, 30),
                    ),
                    elevation=2,
                    margin=0,
                ),
                col=self.col,
                padding=0,
                width=1000,
            )

        return self.card

    async def like_project(self, e):
        self.liked = not self.liked
        await self.update_async()
