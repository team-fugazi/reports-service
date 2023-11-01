from fastapi import APIRouter

from ...models.report import Report
from ...controllers.reports.list import ReportList
from ...controllers.reports.detail import ReportDetail
from ...database.mongodb import database

# Router
router = APIRouter(prefix="/reports", tags=["Reports"])

# Controllers
list_routes = ReportList(database.reports)
detail_routes = ReportDetail(database.reports)


""" List Routes """


@router.get("/")
def get_reports_list():
    return list_routes.get_reports()


@router.post("/")
def post_reports_list(report: Report):
    return list_routes.post_report(report)


@router.put("/")
def put_reports_list():
    return list_routes.put_reports()


@router.delete("/")
def delete_reports_list():
    return list_routes.delete_reports()


""" Detail Routes """


@router.get("/{report_id}")
def get_report_detail(report_id: str):
    return detail_routes.get_report(report_id)


@router.post("/{report_id}")
def post_report_detail():
    return detail_routes.post_report()


@router.put("/{report_id}")
def put_report_detail(report: Report):
    return detail_routes.put_report(report)


@router.delete("/{report_id}")
def delete_report_detail(report_id: str):
    return detail_routes.delete_report(report_id)
