from sqlalchemy import BigInteger, Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    telegram_id = Column(BigInteger, primary_key=True)
    is_banned = Column(Boolean, default=False)
    joined_at = Column(DateTime, default=datetime.datetime.utcnow)

class ChatSession(Base):
    __tablename__ = 'chat_sessions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_a_id = Column(BigInteger, ForeignKey('users.telegram_id'))
    user_b_id = Column(BigInteger, ForeignKey('users.telegram_id'), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class MessageLog(Base):
    """Audit va moderation uchun log. Spam yoki qonunbuzarlik holatlarida admin ko'rishi mumkin."""
    __tablename__ = 'message_logs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(Integer, ForeignKey('chat_sessions.id'))
    sender_id = Column(BigInteger)
    message_id = Column(BigInteger)
    content_type = Column(String) # text, photo, video
    is_reported = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)