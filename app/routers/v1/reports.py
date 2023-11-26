from fastapi import APIRouter

from ...models.report import ReportPartial, Report
from ...models.comment import CommentPartial, Comment
from ...controllers.reports.list import ReportList
from ...controllers.reports.detail import ReportDetail
from ...controllers.reports.special import ReportSpecial
from ...database.mongodb import database

# Models
from ...models.comment import Comment

# Router
router = APIRouter(prefix="/reports", tags=["Reports"])

# Controllers
list_routes = ReportList(database)
detail_routes = ReportDetail(database)
special_routes = ReportSpecial(database)


""" List Routes """


@router.get("/")
def get_reports_list():
    return list_routes.get_reports()


@router.post("/")
def post_reports_list(report: ReportPartial):
    return list_routes.post_reports(report)


@router.put("/")
def put_reports_list():
    return list_routes.put_reports()


@router.put("/comment")
def add_reports_list():
    return list_routes.put_reports()


""" Detail Routes """


@router.get("/{report_id}")
def get_report_detail(report_id: str):
    return detail_routes.get_report(report_id)


@router.post("/{report_id}")
def post_report_detail():
    print("Hit post_report_detail")
    return detail_routes.post_report()


@router.put("/{report_id}")
def put_report_detail(report_id: str, report: Report):
    return detail_routes.put_report(report_id, report)


@router.delete("/{report_id}")
def delete_report_detail(report_id: str):
    return detail_routes.delete_report(report_id)


""" Special Routes """


# Add comment to report
@router.post("/{report_id}/comment", tags=["Functional"])
def add_comment(report_id: str, comment: CommentPartial):
    return special_routes.add_comment(report_id, comment)


# Delete comment from report
@router.delete("/{report_id}/comment/{comment_id}", tags=["Functional"])
def delete_comment(report_id: str, comment_id: str):
    return special_routes.delete_comment(report_id, comment_id)


# Add action to report
@router.post("/{report_id}/action", tags=["Functional"])
def add_action(report_id: str):
    return special_routes.add_action(report_id)


# Delete action from report
@router.delete("/{report_id}/action/{action_id}", tags=["Functional"])
def delete_action(report_id: str, action_id: str):
    return special_routes.delete_action(report_id, action_id)
