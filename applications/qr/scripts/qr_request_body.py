from pydantic import BaseModel
from typing import Optional


class QR(BaseModel):
    id: str
    content: str
    path_under_bucket: Optional[str] = None
