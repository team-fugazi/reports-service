from pydantic import BaseModel, Field

class Attachment(BaseModel):
    attachment_id: str = Field(..., description="Reference to an attachment document")
    url: str = Field(..., description="URL to the attachment")
