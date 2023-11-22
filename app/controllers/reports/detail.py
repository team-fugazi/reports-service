# Path: app/controllers/reports/detail.py

from fastapi import HTTPException, status
from bson import ObjectId

# Models
from ...models.report import ReportPartial, Report

# Transformers
from ...helpers.transformers import transform_mongodb_to_report


class ReportDetail:
    def __init__(self, db):
        self.db = db

    # Get a single report from the database
    def get_report(self, report_id: str) -> Report:
        report = self.db.find_one({"_id": ObjectId(report_id)})

        if not report:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Report with id {report_id} not found",
            )

        return transform_mongodb_to_report(report)

    # Do not allow to CREATE entire report collection
    def post_report(self) -> HTTPException:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail="Use PUT method to update reports",
        )

    # Update a single report in the database
    def put_report(self, report: Report) -> Report:
        update_result = self.db.update_one(
            {"_id": ObjectId(report.report_id)}, {"$set": report.model_dump()}
        )

        if update_result.modified_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Report with id {report.report_id} not found",
            )

        return {"status": status.HTTP_200_OK, "detail": "Report updated successfully"}

    # Delete a single report from the database
    def delete_report(self, report_id: str):
        delete_result = self.db.delete_one({"_id": ObjectId(report_id)})

        if delete_result.deleted_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Report with id {report_id} not found",
            )

        return {"status": status.HTTP_200_OK, "detail": "Report deleted successfully"}
