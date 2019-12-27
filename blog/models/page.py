import datetime
from sqlalchemy import (
    Column,
    Index,
    Integer,
    UnicodeText,
    Unicode,
    DateTime,
)
from blog.models.meta import Base

class Page(Base):
    __tablename__ = 'page'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), unique=True, nullable=False)
    body = Column(UnicodeText, default=u'')
    created = Column(DateTime, default=datetime.datetime.utcnow)
    edited = Column(DateTime, default=datetime.datetime.utcnow)

#Index('my_index', Page.title, unique=True, mysql_length=255)