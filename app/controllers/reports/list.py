from typing import List
from fastapi import HTTPException, status
from pydantic import ValidationError
from bson import ObjectId
from datetime import datetime

# Models
from ...models.report import ReportPartial
from ...models.report import Report


class ReportList:
    def __init__(self, db):
        self.db = db

    # Get all reports from the database
    def get_reports(self) -> List[Report]:
        reports = self.db.reports.find()
        return [Report(**report) for report in reports]

    # Create a new report in the database
    def post_reports(self, report: ReportPartial) -> Report:
        # Convert partial response body to dict
        report = report.model_dump()

        # Add metadata
        report["id"] = None
        report["created_at"] = datetime.now()

        # Add empty lists for content
        report["comments"] = []
        report["actions"] = []

        try:
            report_full = Report(**report)
        except ValidationError as e:
            return {"status": status.HTTP_422_UNPROCESSABLE_ENTITY, "detail": str(e)}
        
        result = self.db.reports.insert_one(
            report_full.model_dump(by_alias=True, exclude=["id"])
        )

        return {"status": status.HTTP_201_CREATED, "obj": "hello"}

    # Do not allow to UPDATE entire report collection
    def put_reports(self) -> HTTPException:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail="Method not allowed for updating multiple reports at once",
        )

    # Do not allow to DELETE entire report collection
    def delete_reports(self) -> HTTPException:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail="Method not allowed for deleting multiple reports at once",
        )
