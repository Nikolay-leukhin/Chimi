import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, TIMESTAMP
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id: int = Column(Integer, primary_key=True, nullable=False)
    name: str = Column(String, nullable=False)
    surname: str = Column(String, nullable=False)
    email: str = Column(String, nullable=False)
    password: str = Column(String, nullable=False)


class Chat(Base):
    __tablename__ = 'chat'

    id: int = Column(Integer, primary_key=True, nullable=False)
    avatar_path: str = Column(String, nullable=True)


class Participant(Base):
    __tablename__ = 'participant'

    id: int = Column(Integer, primary_key=True, nullable=False)
    user_id: int = Column(Integer, ForeignKey('user.id'))
    chat_id: int = Column(Integer, ForeignKey("chat.id"))

    users_relation = relationship('user', backref='participant')
    chat_relation = relationship('chat', backref='participant')


class Message(Base):
    __tablename__ = 'message'

    id: int = Column(Integer, primary_key=True, nullable=False)
    text: str = Column(String, nullable=False)
    user_id: int = Column(Integer, ForeignKey('user.id'))
    chat_id: int = Column(Integer, ForeignKey("chat.id"))
    sent_in: datetime.datetime = Column(TIMESTAMP, nullable=False)

    users_relation = relationship('user', backref='message')
    chat_relation = relationship('chat', backref='message')
