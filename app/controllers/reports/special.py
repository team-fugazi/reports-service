from typing import List
from fastapi import HTTPException, status
from pydantic import ValidationError
from bson import ObjectId
from datetime import datetime

# Models
from ...models.report import Report
from ...models.comment import Comment, CommentPartial
from ...models.action import Action

# Helpers
from ...helpers.meta_generator import generate_meta


class ReportSpecial:
    def __init__(self, db):
        self.db = db

    """ Stats """

    # TODO: optimize with aggregation pipeline
    def get_user_stats(self, user_id: str):
        # Get report count
        report_count = self.db.reports.count_documents({"user": user_id})

        # Get comment count
        comment_count = self.db.comments.count_documents({"user": user_id})

        # Get action count
        action_count = self.db.actions.count_documents({"user": user_id})

        return {
            "status": status.HTTP_200_OK,
            "meta": generate_meta(),
            "data": {
                "reports": report_count,
                "comments": comment_count,
                "actions": action_count,
            },
        }

    """ Comments """

    # Add a comment to a report
    def add_comment(self, report_id: str, comment: CommentPartial) -> Comment:
        # Convert partial response body to dict
        comment_dict = comment.model_dump()

        # Add metadata
        comment_dict["id"] = None
        comment_dict["created_at"] = datetime.now()
        comment_dict["updated_at"] = None
        comment_dict["deleted_at"] = None

        # Validate and create a Comment instance
        comment_full = Comment(**comment_dict)

        print(report_id)
        print(comment_full)

        # Insert comment into the database
        result_comment = self.db.comments.insert_one(
            comment_full.model_dump(by_alias=True, exclude=["id"])
        )

        # Check if comment was created
        if not result_comment.acknowledged:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Comment could not be created",
            )

        # Add comment to report
        result_comment = self.db.reports.update_one(
            {"_id": ObjectId(report_id)},
            {"$push": {"comments": result_comment.inserted_id}},
        )

        print(result_comment.upserted_id)

        return {
            "status": status.HTTP_201_CREATED,
            "meta": generate_meta(),
            "message": "Comment created successfully",
            "data": "Placeholder",
        }

    # Delete a comment from a report
    def delete_comment(self, report_id: str, comment_id: str) -> Comment:
        # Remove comment reference from the report document
        result = self.db.reports.update_one(
            {"_id": ObjectId(report_id)},
            {"$pull": {"comments": ObjectId(comment_id)}},
        )

        # Check if the comment reference was found and removed
        if result.modified_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Comment not found in the report",
            )

        # Delete the comment itself
        comment_result = self.db.comments.delete_one({"_id": ObjectId(comment_id)})

        # Check if the comment was deleted
        if comment_result.deleted_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Comment not found in the database",
            )

        return {
            "status": status.HTTP_201_CREATED,
            "meta": generate_meta(),
            "message": "Comment deleted successfully",
            "deleted_count": comment_result.deleted_count,
        }

    """ Actions """

    # Add an action to a report
    def add_action(self, report_id: str, action: Action) -> Action:
        # Convert partial response body to dict
        action = action.model_dump()

        # Add metadata
        action["id"] = None
        action["created_at"] = datetime.now()

        try:
            action_full = Action(**action)
        except ValidationError as e:
            return {"status": status.HTTP_422_UNPROCESSABLE_ENTITY, "detail": str(e)}

        result = self.db.reports.update_one(
            {"_id": ObjectId(report_id)},
            {
                "$push": {
                    "actions": action_full.model_dump(by_alias=True, exclude=["id"])
                }
            },
        )

        return {"status": status.HTTP_201_CREATED, "obj": "hello"}

    # Delete an action from a report
    def delete_action(self, report_id: str, action_id: str) -> Action:
        result = self.db.reports.update_one(
            {"_id": ObjectId(report_id)},
            {"$pull": {"actions": {"id": ObjectId(action_id)}}},
        )

        return {"status": status.HTTP_200_OK, "obj": "hello"}
