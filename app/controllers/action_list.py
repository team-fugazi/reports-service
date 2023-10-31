from typing import List
from fastapi import HTTPException, status

# Models
from ..models.action import Action


class ActionList:
    def __init__(self, db):
        self.db = db

    # Get all actions from the database
    def get_actions(self) -> List[Action]:
        actions = self.db.find()
        return [Action(**action) for action in actions]

    # Create a new action in the database
    def post_actions(self, action: Action) -> Action:
        action_dict = action.model_dump()
        result = self.db.insert_one(action_dict)
        return {"status": status.HTTP_201_CREATED, "id": str(result.inserted_id)}

    # Do not allow to UPDATE entire action collection
    def put_actions(self) -> HTTPException:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED)

    # Do not allow to DELETE entire action collection
    def delete_actions(self) -> HTTPException:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED)
