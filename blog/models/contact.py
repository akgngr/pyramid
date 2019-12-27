import datetime
from blog.models.meta import Base
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    UnicodeText,
    DateTime
)

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    user = Column(Unicode(255), unique=False, nullable=False)
    title = Column(Unicode(255), unique=False, nullable=False)
    body = Column(UnicodeText, default=u'')
    created = Column(DateTime, default=datetime.datetime.utcnow)
