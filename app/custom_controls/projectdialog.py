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
    Markdown,
    IconButton,
    icons,
    border_radius,
    border,
    colors,
    padding,
    alignment,
    margin
)

from ..class_project import Project


class DialogContent(UserControl):
    def __init__(
        self,
        project: Project,
        flag_my_project: bool = False,
        liked: bool = False
    ):
        super().__init__()
        self.project = project
        self.flag_my_project = flag_my_project
        self.liked = liked

    def build(self):
        # container for dialog actions
        self.actions_container = \
            Container(
                Row(
                    [
                        IconButton(
                            icon="edit",
                            visible=self.flag_my_project,
                        ),
                        IconButton(
                            icon="save",
                            visible=self.flag_my_project,
                        ),
                        IconButton(
                            icon="delete",
                            visible=self.flag_my_project,
                        ),
                        IconButton(
                            icon="share",
                        ),
                        IconButton(
                            icon="close",
                        )
                    ]
                )
            )

        # container for upper row
        self.upper_row = \
            Row(
                [
                    Text(self.project.title),
                    self.actions_container,
                ],
                alignment=MainAxisAlignment.SPACE_BETWEEN
            )

        # container for project description
        self.project_description = \
            Container(
                content=Markdown(
                    self.project.description
                )
            )

        # container for project hashtags
        self.project_hashtags = \
            Container(
                Row(
                    [
                        Text(
                            "Hashtags: ",
                        ),
                        *[
                            Text(
                                tag,
                            )
                            for tag in self.project.tags
                        ],
                        IconButton(
                            icon="add",
                        )
                    ]
                )
            )

        # container for likes
        self.project_likes = \
            Container(
                TextButton(
                    text=(str(self.project.likes + int(self.liked)) + " 🔥"),
                    #on_click=self.like_project,
                )
            )

        # main column
        self.main_column = \
            Container(
                Column(
                    [
                        self.upper_row,
                        Divider(),
                        self.project_description,
                        Divider(),
                        self.project_hashtags,
                        self.project_likes,
                    ],
                    width=1000,
                )
            )

        return self.main_column


# TODO вот этот костыль на что-то адекватное
def get_project_dialog(project: Project, **kwargs):
    ad = AlertDialog(
        content=DialogContent(
            project=project,
            **kwargs
        )
    )

    return ad
