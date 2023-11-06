from pydantic import BaseModel, Field
from typing import Optional

class Attachment(BaseModel):
    id: Optional[str] = Field(..., description="MongoDB Object ID of the document")
    url: str = Field(..., description="URL to the attachment")
    description: Optional[str] = Field(None, description="Attachment description")
