from pydantic import BaseModel
from datetime import datetime

class WallPostPydantic(BaseModel):
    content: str

class WallGetPydantic(BaseModel):
    id: int
    content: str
    created_at: datetime
