from pydantic import BaseModel, Field

class Action(BaseModel):
    action_id: str = Field(..., description="Reference to an action document")
    action_type: str = Field(..., description="Type of moderation action")
    moderator_id: str = Field(..., description="ID of the moderator who took the action")