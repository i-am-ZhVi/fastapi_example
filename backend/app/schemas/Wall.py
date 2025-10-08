from pydantic import BaseModel
from datetime import datetime

class WallPost(BaseModel):
    content: str

class WallGet(WallPost):
    id: int
    userid: int
    created_at: datetime
