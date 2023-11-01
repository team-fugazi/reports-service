from pydantic import BaseModel, Field
from bson import ObjectId

class Category(BaseModel):
    id: str = Field(..., description="MongoDB Object ID of the document")
    category_id: str = Field(..., description="Reference to a category document")
    name: str = Field(..., description="Category name")
    description: str = Field(..., description="Category description")