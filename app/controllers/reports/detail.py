# Path: app/controllers/reports/detail.py

from fastapi import HTTPException, status
from pydantic import ValidationError
from bson import ObjectId

# Helpers
from ...helpers.meta_generator import generate_meta

# Models
from ...models.report import ReportPartial, Report, ReportFull
from ...models.comment import Comment


class ReportDetail:
    def __init__(self, db):
        self.db = db

    # Get a single report from the database
    def get_report(self, report_id: str) -> Report:
        report = self.db.reports.find_one({"_id": ObjectId(report_id)})

        if not report:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Report with id {report_id} not found",
            )

        # Populate category field
        category_full = self.db.categories.find_one(
            {"_id": ObjectId(report["category"])}
        )
        report["category"] = category_full

        # Populate comments field
        comments_ids = report.get("comments", [])
        comments_full = self.db.comments.find({"_id": {"$in": comments_ids}})
        report["comments"] = [Comment(**comment) for comment in comments_full]

        return {
            "status": status.HTTP_200_OK,
            "meta": generate_meta(),
            "data": ReportFull(**report),
        }

    # Update a single report in the database TODO: maybe should receive a ReportPartial
    def put_report(self, report_id: str, report: Report) -> dict:
        # Check if report exists
        existing_report = self.db.reports.find_one({"_id": ObjectId(report_id)})
        if not existing_report:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Report with id {report_id} not found",
            )

        # Update report
        update_fields = report.model_dump(
            by_alias=True, exclude=["id"], exclude_unset=True
        )
        result = self.db.reports.update_one(
            {"_id": ObjectId(report_id)}, {"$set": update_fields}
        )

        # Check if report was modified
        if result.modified_count == 0:
            raise HTTPException(
                status_code=status.HTTP_304_NOT_MODIFIED,
                detail=f"Report with id {report_id} not modified",
            )

        # Fetch the updated report from the database
        updated_report = self.db.reports.find_one({"_id": ObjectId(report_id)})

        return {
            "status": status.HTTP_200_OK,
            "meta": generate_meta(),
            "message": "Resource updated successfully",
            "data": Report(**updated_report),
        }

    # Delete a single report from the database
    def delete_report(self, report_id: str):
        delete_result = self.db.reports.delete_one({"_id": ObjectId(report_id)})

        if delete_result.deleted_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Report with id {report_id} not found",
            )

        return {"status": status.HTTP_200_OK, "detail": "Report deleted successfully"}
