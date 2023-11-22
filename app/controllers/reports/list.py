from typing import List
from fastapi import HTTPException, status
from pydantic import ValidationError
from datetime import datetime
from bson import ObjectId

# Helpers
from ...helpers.meta_generator import generate_meta

# Models
from ...models.report import ReportPartial
from ...models.report import Report


class ReportList:
    def __init__(self, db):
        self.db = db

    # Get all reports from the database
    def get_reports(self) -> List[Report]:
        reports_cursor = self.db.reports.find()

        # get document count
        num_documents = self.db.reports.count_documents({})

        # modify metadata to include return count
        modified_meta = generate_meta()
        modified_meta["total_count"] = num_documents

        return {
            "status": status.HTTP_200_OK,
            "meta": modified_meta,
            "data": [Report(**report) for report in reports_cursor],
        }

    # Create a new report in the database
    def post_reports(self, report_partial: ReportPartial) -> Report:
        # Convert partial response body to dict
        report_dict = report_partial.model_dump()

        # Add metadata
        report_dict["id"] = None
        report_dict["created_at"] = datetime.now()

        # Add empty lists for content
        report_dict["comments"] = []
        report_dict["actions"] = []

        # Validate and create a Report instance
        report_full = Report(**report_dict)

        # Insert report into the database
        result = self.db.reports.insert_one(
            report_full.model_dump(by_alias=True, exclude=["id"])
        )

        # Check if report was created
        if not result.acknowledged:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Report could not be created",
            )

        # Fetch the inserted report from the database
        inserted_report = self.db.reports.find_one(
            {"_id": ObjectId(result.inserted_id)}
        )

        return {
            "status": status.HTTP_201_CREATED,
            "meta": generate_meta(),
            "message": "Resource created successfully",
            "data": Report(**inserted_report),
        }

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
