from pydantic import BaseModel, Field

class Category(BaseModel):
    category_id: str = Field(..., description="Reference to a category document")
    name: str = Field(..., description="Category name")
    description: str = Field(..., description="Category description")