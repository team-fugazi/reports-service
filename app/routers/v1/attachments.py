from fastapi import APIRouter

from ...models.attachment import Attachment
from ...controllers.attachments.list import AttachmentList

# from ...controllers.attachments.detail import AttachmentDetail
from ...database.mongodb import database

# Router
router = APIRouter(prefix="/attachments", tags=["Attachments"])

# Controllers
list_routes = AttachmentList(database.attachments)
# detail_routes = AttachmentDetail(database.attachments)


# Controllers added to Routes
@router.get("/")
def get_attachments_list():
    return list_routes.get_attachments()


@router.post("/")
def post_attachments_list(attachment: Attachment):
    return list_routes.post_attachments(attachment)


@router.put("/")
def put_attachments_list():
    return list_routes.put_attachments()


@router.delete("/")
def delete_attachments_list():
    return list_routes.delete_attachments()
