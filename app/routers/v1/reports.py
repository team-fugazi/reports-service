from fastapi import APIRouter

from ...models.report import Report
from ...controllers.report_list import ReportList
from ...database.mongodb import database

# Router
router = APIRouter(prefix="/reports", tags=["Reports", "v1"])

# Controllers
list_routes = ReportList(database.reports)


# Controllers added to Routes
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


"""
@router.post("/{id}", tags=["Detail"])
def post_service_detail():
    return detail_routes.create_service()


@router.get("/{id}", tags=["Detail"])
def get_service_detail(id: str):
    return detail_routes.get_service(id)


@router.put("/{id}", tags=["Detail"])
def put_service_detail(id: str, service: Service):
    return detail_routes.update_service(id, service)


@router.delete("/{id}", tags=["Detail"])
def delete_service_detail(id: str):
    return detail_routes.delete_service(id) """
