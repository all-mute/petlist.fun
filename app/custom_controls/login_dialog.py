from flet import (
    UserControl,
    Column,
    Row,
    Card,
    TextButton,
    FloatingActionButton,
    ElevatedButton,
    TextThemeStyle,
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


class DialogContent(UserControl):
    def __init__(
        self,
        **kwargs
    ):
        super().__init__()

    def build(self):
        # "LOGIN" text
        self.big_text = \
            Row(
                [
                    Text(
                        "Login",
                        style=TextThemeStyle.DISPLAY_MEDIUM
                    )
                ],
                alignment=alignment.center,
                expand=True,
            )

        # email field
        self.email_field = \
            TextField(
                label="Email",
                expand=True,
            )

        # password field
        self.password_field = \
            TextField(
                label="Password",
                expand=True,
                password=True,
                can_reveal_password=True,
            )

        # login button
        self.button_login = \
            OutlinedButton(
                content=Text("Login"),
                icon=icons.CHECK,
                expand=True
            )

        # sign up button
        self.button_sign_up = \
            OutlinedButton(
                content=Text("Sign up"),
                icon=icons.LOGIN,
                expand=True
            )

        # action buttons row
        self.action_buttons_row = \
            Row(
                [
                    self.button_login,
                    self.button_sign_up,
                ],
            )

        # main column
        self.main_column = \
            Container(
                Column(
                    [
                        self.big_text,
                        self.email_field,
                        self.password_field,
                        self.action_buttons_row,
                        # self.alternative_action_button
                    ],
                    width=600,
                )
            )

        return self.main_column

        # TODO вот этот костыль на что-то адекватное

    def get_project_dialog(**kwargs):
        ad = AlertDialog(
            content=DialogContent(
                **kwargs
            ),
            # inset_padding=padding.symmetric(vertical=24, horizontal=4),
        )

        return ad