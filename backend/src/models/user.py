from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from datetime import datetime

from typing import Optional

from constants import text_max, char_max, char_min

class User(Base):
    __tablename__ = 'user'


    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(String(char_max))

    display_name: Mapped[Optional[str]] = mapped_column(String(char_max))

    email: Mapped[str] = mapped_column(String(254), unique=True) # Именно столько потому что в email максимум столько символов согласно SMTP

    password: Mapped[str] = mapped_column(String())

    registration_moment: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    bio: Mapped[Optional[str]] = mapped_column(String(text_max))

    messages: Mapped[list['Message']] = relationship(back_populates='user')

