from app.class_project import Project


def get_projects(email: str, hashtags: list[str]):
    if hashtags:
        get_projects_with_hashtags(email)
    else:
        get_all_projects()


def get_projects_with_hashtags(email: str):
    pass


def get_all_projects():
    pass


def like_project(email: str, project_id: int):
    pass


def dislike_project(email: str, project_id: int):
    pass


def is_user_in_database(email: str):
    pass


def authentication(email: str):
    if not is_user_in_database(email):
        sign_up(email)


def sign_up(email: str):
    pass


def create_project(email: str, new_project: Project):
    pass


def update_project(email: str, project_id: int, new_project: Project):
    pass


def delete_project(email: str, project_id: int):
    pass






