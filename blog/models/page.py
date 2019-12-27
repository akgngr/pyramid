from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

class Page(object):
    def __init__(self, title, uri, body, owner):
        self.title = title
        self.uri = uri
        self.body = body
        self.owner = owner