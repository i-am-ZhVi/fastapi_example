from datetime import datetime
from pydantic import BaseModel


class MessagePost(BaseModel):
    userid: int
    content: str

class MessageGet(BaseModel):
    id: int
    create_at: datetime
