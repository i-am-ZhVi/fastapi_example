from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from datetime import datetime

from sqlalchemy.sql import text

from models import Base


class PrivateMessage(Base):
    __tablename__ = "private_messages"
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(), server_default=text("TIMEZONE('utc', now())"))

    sender: Mapped["User"] = relationship(back_populates="private_messages_sent")
    recipient: Mapped["User"] = relationship(back_populates="private_messages_received")
    chat: Mapped["Chat"] = relationship(back_populates="private_messages")
