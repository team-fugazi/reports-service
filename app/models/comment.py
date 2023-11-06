from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# fmt: off
class Comment(BaseModel):
    user_id: str = Field(..., description="ID of the user who made the comment")
    content: str = Field(..., description="Comment content")
    created_at: datetime = Field(..., description="Date and time the comment was created")
    updated_at: Optional[datetime] = Field(None, description="Date and time the comment was last updated (optional)")
    deleted_at: Optional[datetime] = Field(None, description="Date and time the comment was deleted (optional)")
