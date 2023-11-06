# Path: app/models/action.py
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import datetime


class ModerationActionType(str, Enum):
    remove = "remove"
    warn = "warn"
    suspend = "suspend"
    ban = "ban"
    edit_content = "edit_content"
    require_approval = "require_approval"
    content_warning = "content_warning"


# fmt: off
class Action(BaseModel):
    id: Optional[str] = Field(..., description="MongoDB Object ID of the document")
    action_type: ModerationActionType = Field(..., description="Type of moderation action")
    user_id: str = Field(..., description="ID of the user the action is taken against")
    moderator_id: str = Field(..., description="ID of the moderator who initiated the action")
    reason: str = Field(..., description="A brief description of the reason for the action")
    details: Optional[str] = Field(None, description="Additional details or comments (optional)")
    created_at: datetime = Field(..., description="Date and time the action was initiated")
    expires_at: datetime = Field(None, description="Date and time the action expires (optional)")
