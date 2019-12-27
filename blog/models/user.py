from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

class User(object):
    def __init__(self, login, password, groups=None):
        self.login = login
        self.password = password
        self.groups = groups or []

    def check_password(self, passwd):
        return self.password == passwd
