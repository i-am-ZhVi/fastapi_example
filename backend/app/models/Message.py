from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import text
from models import Base

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    content = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=text("TIMEZONE('utc', now())"))
