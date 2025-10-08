from datetime import datetime
from pydantic import BaseModel


class MessagePost(BaseModel):
    content: str

class MessageGet(MessagePost):
    id: int
    userid: int
    created_at: datetime
