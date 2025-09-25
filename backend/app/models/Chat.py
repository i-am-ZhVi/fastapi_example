from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from datetime import datetime

from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql import text

from models import Base

class Chat(Base):
    __tablename__ = "chats"
    id: Mapped[int] = mapped_column(primary_key=True)
    isgroup: Mapped[bool] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=True)
    creatorid: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    createdat: Mapped[datetime] = mapped_column(default=datetime.now(), server_default=text("TIMEZONE('utc', now())"))

    creator: Mapped["User"] = relationship(back_populates="chats")
    members: Mapped[list["ChatMember"]] = relationship(back_populates="chat")
    messages: Mapped["Message"] = relationship(back_populates="chat")
