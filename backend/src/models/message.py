from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

from datetime import datetime

from constants import char_max

class Message(Base):
    __tablename__ = 'message'


    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id', ondelete='CASCADE'))

    chat_id: Mapped[int] = mapped_column(ForeignKey('chat.id', ondelete='CASCADE'))

    text: Mapped[str] = mapped_column(String(char_max))

    sent_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    user: Mapped['User'] = relationship(back_populates='messages')
    