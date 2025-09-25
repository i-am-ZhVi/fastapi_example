from pydantic import BaseModel
from datetime import datetime

class PrivateMessagePost(BaseModel):
    content: str
    senderid: int
    recipientid: int
    content: str


class PrivateMessageGet(PrivateMessagePost):
    id: int
    create_at: datetime
