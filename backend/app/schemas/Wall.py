from pydantic import BaseModel
from datetime import datetime

class WallPost(BaseModel):
    userid: int
    content: str

class WallGet(WallPost):
    id: int
    created_at: datetime
