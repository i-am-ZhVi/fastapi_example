from datetime import datetime
from pydantic.main import BaseModel


class ChatPost(BaseModel):
    isgroup: bool
    name: str
    creatorid: int

class ChatGet(ChatPost):
    id: int
    createdat: datetime
