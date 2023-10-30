from typing import List
from fastapi import HTTPException, status

# Models
from ..models.report import Report

class ReportList:
    def __init__(self, db):
        self.db = db

    # Get all reports from the database 
    def get_reports(self) -> List[Report]:
        reports = self.db.find()
        return [Report(**report) for report in reports]
    
    # Create a new report in the database
    def post_reports(self, report: Report) -> Report:
        report_dict = report.model_dump()
        result = self.db.insert_one(collection="reports", data=report_dict)
        return {"status": status.HTTP_201_CREATED, "id": str(result.inserted_id)}
    
    # Do not allow to UPDATE entire report collection
    def put_reports(self) -> HTTPException:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED)

    # Do not allow to DELETE entire report collection
    def delete_reports(self) -> HTTPException:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED)