from flet import (
    UserControl,
    Column,
    Row,
    border,
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


class AddOutlinedIconButton(UserControl):
    def __init__(
        self,
    ):
        super().__init__()

    def build(self):
        # container for add button
        self.container_for_add = \
            Container(
                Container(
                    Icon("add", scale=1),
                    border=border.all(1, color=colors.OUTLINE),
                    border_radius=20,
                    alignment=alignment.center,
                    padding=padding.symmetric(vertical=6, horizontal=12),
                    opacity=1
                ),
                alignment=alignment.center
            )

        return self.container_for_add


