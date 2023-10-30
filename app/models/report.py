from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

# Sub models
from .action import Action
from .attachment import Attachment
from .category import Category
from .comment import Comment

# Report model
class Report(BaseModel):
    report_id: str = Field(..., description="Unique report identifier")
    user_id: str = Field(..., description="User ID who submitted the report")
    category: Category
    comments: List[Comment] = []
    attachments: List[Attachment] = []
    actions: List[Action] = []
    description: str = Field(..., description="Report description")
    created_at: datetime = Field(..., description="Timestamp of report submission")

    class Config:
        json_schema_extra = {
            "example": {
                "report_id": "unique_report_id",
                "user_id": "google-oauth2|115381085628553582032",
                "category": {
                    "category_id": "category_id_1",
                    "name": "Offensive Content"
                },
                "comments": [],
                "attachments": [],
                "actions": [],
                "description": "This is a report about offensive content.",
                "created_at": "2023-10-30T12:00:00"
            }
        }
