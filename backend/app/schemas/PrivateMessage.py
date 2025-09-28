from pydantic import BaseModel
from datetime import datetime

class PrivateMessagePost(BaseModel):
    content: str
    senderid: int
    recipientid: int


class PrivateMessageGet(PrivateMessagePost):
    id: int
    created_at: datetime
