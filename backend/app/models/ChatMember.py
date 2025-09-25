from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from datetime import datetime

from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql import text

from models import Base


class ChatMember(Base):
    __tablename__ = "chatmembers"
    id: Mapped[int] = mapped_column(primary_key=True)
    chatid: Mapped[int] = mapped_column(ForeignKey("chats.id"), nullable=False)
    userid: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    joinedat: Mapped[datetime] = mapped_column(default=datetime.now(), server_default=text("TIMEZONE('utc', now())"))

    chat: Mapped["Chat"] = relationship(back_populates="members")
    user: Mapped["User"] = relationship(back_populates="chats")
