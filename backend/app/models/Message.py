from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from datetime import datetime

from sqlalchemy.sql import text
from sqlalchemy.schema import ForeignKey

from models import Base


class Message(Base):
    __tablename__ = "messages"
    id: Mapped[int] = mapped_column(primary_key=True)
    userid: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(), server_default=text("TIMEZONE('utc', now())"))

    sender: Mapped["User"] = relationship(back_populates="messages")
