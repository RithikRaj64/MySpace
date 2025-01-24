from pydantic import BaseModel
from datetime import datetime

class Thread(BaseModel):
    username: str
    content: str
    vibe: str
    created_at: datetime