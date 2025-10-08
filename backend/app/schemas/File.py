

from datetime import datetime
from pydantic import BaseModel


class FilePost(BaseModel):
    filename: str
    content: str

class FileGet(FilePost):
    id: int
    uploaderid: int
    created_at: datetime
