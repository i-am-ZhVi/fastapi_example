

from datetime import datetime
from pydantic import BaseModel


class FilePost(BaseModel):
    uploaderid: int
    filename: str
    content: str

class FileGet(FilePost):
    id: int
    created_at: datetime
