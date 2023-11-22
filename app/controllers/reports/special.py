from typing import List
from fastapi import HTTPException, status
from pydantic import ValidationError
from bson import ObjectId
from datetime import datetime

# Models
from ...models.report import Report
from ...models.comment import Comment
from ...models.action import Action


class ReportSpecial:
    def __init__(self, db):
        self.db = db

    """ Comments """

    # Add a comment to a report
    def add_comment(self, report_id: str, comment: Comment) -> Comment:
        # Convert partial response body to dict
        comment = comment.model_dump()

        # Add metadata
        comment["id"] = None
        comment["created_at"] = datetime.now()

        try:
            comment_full = Comment(**comment)
        except ValidationError as e:
            return {"status": status.HTTP_422_UNPROCESSABLE_ENTITY, "detail": str(e)}

        result = self.db.reports.update_one(
            {"_id": ObjectId(report_id)},
            {
                "$push": {
                    "comments": comment_full.model_dump(by_alias=True, exclude=["id"])
                }
            },
        )

        return {"status": status.HTTP_201_CREATED, "obj": "hello"}

    # Delete a comment from a report
    def delete_comment(self, report_id: str, comment_id: str) -> Comment:
        result = self.db.reports.update_one(
            {"_id": ObjectId(report_id)},
            {"$pull": {"comments": {"id": ObjectId(comment_id)}}},
        )

        return {"status": status.HTTP_200_OK, "obj": "hello"}

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

    """ Search """

    # Search reports
    def search_reports(self, query: str) -> List[Report]:
        reports = self.db.reports.find(
            {"$text": {"$search": query}},
            {"score": {"$meta": "textScore"}},
        )
        return [Report(**report) for report in reports]
