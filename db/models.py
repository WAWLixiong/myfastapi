from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean

from db.database import Base


# model definition
class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50))
    email = Column(String(50))
    password = Column(String(100))
    items = relationship('DbArticle', back_populates='user')


class DbArticle(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(50))
    content = Column(String(255))
    published = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("DbUser", back_populates='items')
