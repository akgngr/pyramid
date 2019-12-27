import datetime #<- will be used to set default dates on models
from blog.models.meta import Base  #<- we need to import our sqlalchemy metadata from which model classes will inherit
from sqlalchemy import (
    Index,
    Text,
    Column,
    Integer,
    Unicode,     #<- will provide Unicode field
    UnicodeText, #<- will provide Unicode text field
    DateTime,    #<- time abstraction field

)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(Unicode(100), nullable=True)
    name = Column(Unicode(255), unique=True, nullable=False)
    password = Column(Unicode(255), nullable=False)
    last_logged = Column(DateTime, default=datetime.datetime.utcnow)

#Index('user_index', User.email, unique=True, mysql_length=255)