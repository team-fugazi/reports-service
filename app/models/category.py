# Path: app/models/category.py
from typing import Optional
from typing_extensions import Annotated
from pydantic import BaseModel, Field
from pydantic.functional_validators import BeforeValidator

# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]

class Category(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)   
    category_id: int = Field(..., description="Reference to a category document")
    name: str = Field(..., description="Category name")
    description: str = Field(..., description="Category description")