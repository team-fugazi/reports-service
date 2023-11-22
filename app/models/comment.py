from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]

# fmt: off

# Partial comment model: used for sparse body requests
class CommentPartial(BaseModel):
    user: str = Field(..., description="ID of the user who made the comment")
    content: str = Field(..., description="Comment content")

# Comment model: used for full comments
class Comment(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)   
    user: str = Field(..., description="ID of the user who made the comment")
    content: str = Field(..., description="Comment content")
    created_at: datetime = Field(..., description="Date and time the comment was created")
    updated_at: Optional[datetime] = Field(None, description="Date and time the comment was last updated (optional)")
    deleted_at: Optional[datetime] = Field(None, description="Date and time the comment was deleted (optional)")
# fmt: on
