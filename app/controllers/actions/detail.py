from typing import List
from fastapi import HTTPException, status

# Models
from ...models.action import Action


class ActionDetail:
    def __init__(self, db):
        self.db = db

    # Get a single action from the database
    def get_action(self, action_id: str) -> Action:
        action = self.db.find_one({"_id": action_id})
        if action:
            return Action(**action)
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Action with id {action_id} not found",
            )

    # Do not allow to CREATE entire action collection
    def post_action(self) -> HTTPException:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail="Method not allowed for creating actions",
        )

    # Update a single action in the database
    def put_action(self, action_id: str, action: Action) -> Action:
        action_dict = action.model_dump()
        result = self.db.update_one({"_id": action_id}, {"$set": action_dict})
        if result.modified_count == 1:
            return {"status": status.HTTP_200_OK}
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Action with id {action_id} not found",
            )

    # Delete a single action from the database
    def delete_action(self, action_id: str) -> Action:
        result = self.db.delete_one({"_id": action_id})
        if result.deleted_count == 1:
            return {"status": status.HTTP_200_OK}
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Action with id {action_id} not found",
            )
