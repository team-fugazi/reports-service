from pydantic import BaseModel, Field

class Comment(BaseModel):
    comment_id: str = Field(..., description="Reference to a comment document")
    content: str = Field(..., description="Comment content")