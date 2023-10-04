from datetime import datetime


class Project:
    def __init__(self, author, title, description, likes, tags, public, liked_by_user):
        self._author = author
        self._title = title
        self._description = description
        self._likes = likes
        self._tags = tags
        self._created_at = datetime.now()
        self._updated_at = datetime.now()
        self._public = public
        self._liked_by_user = liked_by_user

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self, value):
        self._likes = value

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        self._tags = value

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at

    @property
    def public(self):
        return self._public

    @public.setter
    def public(self, value):
        self._public = value

    @property
    def liked_by_user(self):
        return self._liked_by_user

    @liked_by_user.setter
    def liked_by_user(self, value):
        self._liked_by_user = value

    def update(self, title=None, description=None, likes=None, tags=None, public=None):
        self.title = title if title is not None else self.title
        self.description = description if description is not None else self.description
        self.likes = likes if likes is not None else self.likes
        self.tags = tags if tags is not None else self.tags
        self._updated_at = datetime.now()
        self.public = public if public is not None else self.public

    def __str__(self):
        return f"Author: {self.author}\nTitle: {self.title}\nDescription: {self.description}\nLikes: {self.likes}\nTags: {self.tags}\nCreated At: {self.created_at}\nUpdated At: {self.updated_at}\nPublic: {self.public}\nLiked By User: {self.liked_by_user}"


default_project = Project(
    author="John Doe",
    title="my project" * 6,
    description="This is a sample project",
    likes=0,
    tags=["#ml", "#open"],
    public=True,
    liked_by_user=False,
)

default_project2 = Project(
    author="John Doe",
    title="my project",
    description="This is a sample project",
    likes=0,
    tags=["#ml", "#open"],
    public=True,
    liked_by_user=False,
)

"""print(default_project)
["rwvev"] * 10000000
default_project.update()
print(default_project)"""