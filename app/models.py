from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    username = Column(String, nullable=True)
    city = Column(String, nullable=True)
    sphere = Column(String, nullable=True)
    description = Column(String, nullable=True)
    category = Column(String, nullable=True)

    likes_sent = relationship('Swipe', back_populates='from_user', foreign_keys='Swipe.from_user_id')
    likes_received = relationship('Swipe', back_populates='to_user', foreign_keys='Swipe.to_user_id')

class Swipe(Base):
    __tablename__ = 'swipes'

    id = Column(Integer, primary_key=True)
    from_user_id = Column(Integer, ForeignKey('users.id'))
    to_user_id = Column(Integer, ForeignKey('users.id'))
    is_like = Column(Boolean, default=False)

    from_user = relationship('User', back_populates='likes_sent', foreign_keys=[from_user_id])
    to_user = relationship('User', back_populates='likes_received', foreign_keys=[to_user_id])
