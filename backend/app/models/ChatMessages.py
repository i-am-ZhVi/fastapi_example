
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm.base import Mapped
from sqlalchemy.schema import ForeignKey
from models import Base

class ChatMessages(Base):
    __tablename__ = "chat_messages"
    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"), primary_key=True, nullable=False)
    message_id: Mapped[int] = mapped_column(ForeignKey("messages.id"), primary_key=True, nullable=False)
