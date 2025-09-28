from datetime import datetime
from pydantic import BaseModel


class MessagePost(BaseModel):
    userid: int
    content: str

class MessageGet(MessagePost):
    id: int
    created_at: datetime
