from pydantic import BaseModel
from datetime import datetime

class PrivateMessagePost(BaseModel):
    content: str
    recipientid: int


class PrivateMessageGet(PrivateMessagePost):
    id: int
    senderid: int
    created_at: datetime
