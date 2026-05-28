import enum

from sqlalchemy import String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

from datetime import datetime

class RoleEnum(enum.Enum):
    OWNER = 'OWNER'
    ADMIN = 'ADMIN'
    USER = 'USER'

class UserToChat(Base):
    __tablename__ = 'user_to_chat'


    user_id: Mapped[int] = mapped_column(ForeignKey('user.id', ondelete='CASCADE'), primary_key=True)

    chat_id: Mapped[int] = mapped_column(ForeignKey('chat.id', ondelete='CASCADE'), primary_key=True)

    joined_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    role: Mapped[RoleEnum] = mapped_column(Enum(RoleEnum))

