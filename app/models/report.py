from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

# Sub models
from .action import Action
from .comment import Comment

# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]


# Report Request Model
class ReportPartial(BaseModel):
    description: str = Field(..., description="Report description")                 # Metadata
    original_post: str = Field(..., description="URL to the original post")         # Metadata
    category: str = Field(..., description="Document Reference to the category")    # Metadata
    category: str = Field(..., description="Document Reference to the category")    # Reference
    user: str = Field(..., description="Document Reference to the user")            # Reference

    # class Config:
    #     json_schema_extra = {
    #         "example": {
    #             "user": "google-oauth2|115381085628553582032",
    #             "category": "6540fc65949a5dae09a77e25",
    #             "original_post": "https://www.reddit.com/r/rust/comments/181aw3o/what_safety_features_does_rust_offer_that_c_doesnt",
    #             "description": "This is a report about offensive content.",
    #         }

# Report model
class Report(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)                     # Metadata
    description: str = Field(..., description="Report description")                 # Metadata
    original_post: str = Field(..., description="URL to the original post")         # Metadata
    created_at: datetime = Field(..., description="Timestamp of report submission") # Metadata
    user: str = Field(..., description="Document Reference to the user")            # Reference
    category: str = Field(..., description="Document Reference to the category")    # Reference
    comments: List[Comment] = []                                                    # Content
    actions: List[Action] = []                                                      # Content

    # class Config:
    #     json_schema_extra = {
    #         "example": {
    #             "id": "60f7b4e8e6d9d9a9a9a9a9a9",
    #             "report_id": "unique_report_id",
    #             "user_id": "google-oauth2|115381085628553582032",
    #             "description": "This is a report about offensive content.",
    #             "original_post": "https://www.reddit.com/r/rust/comments/181aw3o/what_safety_features_does_rust_offer_that_c_doesnt",
    #             "created_at": "2023-10-30T12:00:00",
    #             "category": {
    #                 "id": "6540fc65949a5dae09a77e25",
    #                 "category_id": 1,
    #                 "name": "Offensive Content",
    #                 "description": "Category Description",
    #             },
    #             "comments": [
    #                 {
    #                     "id": "60f7b4e8e6d9d9a9a9a9a9a9",
    #                     "comment_id": "unique_comment_id",
    #                     "user_id": "google-oauth2|115381085628553582032",
    #                     "body": "This is a comment about offensive content.",
    #                     "created_at": "2023-10-30T12:00:00",
    #                 }
    #             ],
    #             "actions": [
    #                 {
    #                     "id": "60f7b4e8e6d9d9a9a9a9a9a9",
    #                     "action_id": "unique_action_id",
    #                     "user_id": "google-oauth2|115381085628553582032",
    #                     "action": "Reported",
    #                     "created_at": "2023-10-30T12:00:00",
    #                 }
    #         }
    #     }
