import enum

from constants import char_max

from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column
from database import Base



class ChatTypeEnum(str, enum.Enum):
    DIRECT = 'DIRECT'
    GROUP = 'GROUP'

class Chat(Base):
    __tablename__ = 'chat'


    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(char_max))

    type: Mapped[ChatTypeEnum] = mapped_column(Enum(ChatTypeEnum))
