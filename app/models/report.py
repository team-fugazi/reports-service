from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

# Sub models
from .action import Action
from .comment import Comment
from .category import Category

# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]


# Partial Report model: used for sparse body requests
class ReportPartial(BaseModel):
    description: str = Field(..., description="Report description")                 # Metadata
    original_post: str = Field(..., description="URL to the original post")         # Metadata
    category: str = Field(..., description="Document Reference to the category")    # Metadata
    category: str = Field(..., description="Document Reference to the category")    # Reference
    user: str = Field(..., description="Document Reference to the user")            # Reference


# Report model: used for full reports
class Report(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)                     # Metadata
    description: str = Field(..., description="Report description")                 # Metadata
    original_post: str = Field(..., description="URL to the original post")         # Metadata
    created_at: datetime = Field(..., description="Timestamp of report submission") # Metadata
    user: str = Field(..., description="Document Reference to the user")            # Reference
    category: str = Field(..., description="Document Reference to the category")    # Reference
    comments: List[PyObjectId] = []                                                    # Content
    actions: List[Action] = []    
    

# Report model: used for full reports
class ReportFull(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)                     # Metadata
    description: str = Field(..., description="Report description")                 # Metadata
    original_post: str = Field(..., description="URL to the original post")         # Metadata
    created_at: datetime = Field(..., description="Timestamp of report submission") # Metadata
    user: str = Field(..., description="Document Reference to the user")            # Reference
    category: Category = Field(..., description="Document Reference to the category")    # Reference
    comments: List[Comment] = []                                                    # Content
    actions: List[Action] = []   
                                                  # Content
