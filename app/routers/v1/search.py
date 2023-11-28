from fastapi import APIRouter, status

from ...models.report import ReportPartial, Report

# utils
from ...helpers.meta_generator import generate_meta

# database
from ...database.mongodb import database

# Router
router = APIRouter(prefix="/search", tags=["Search"])

# Controllers


@router.get("/reports")
def search_reports(query: str = ""):
    pipeline = [
        {
            "$search": {
                "index": "default",
                "text": {"query": query, "path": {"wildcard": "*"}},
            }
        }
    ]

    print(query)

    # Search reports
    aggregate_result = database.reports.aggregate(pipeline)
    results = [Report(**report) for report in aggregate_result]

    return {
        "status": status.HTTP_200_OK,
        "meta": generate_meta(),
        "data": results,
    }
