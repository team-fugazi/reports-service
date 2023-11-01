from fastapi import APIRouter

from ...models.attachment import Attachment
from ...controllers.attachments.list import AttachmentList
from ...controllers.attachments.detail import AttachmentDetail
from ...database.mongodb import database

# Router
router = APIRouter(prefix="/attachments", tags=["Attachments"])

# Controllers
list_routes = AttachmentList(database.attachments)
detail_routes = AttachmentDetail(database.attachments)


""" List Routes """


# Get all attachments from the database
@router.get("/")
def get_attachments_list():
    return list_routes.get_attachments()


# Create a new attachment in the database
@router.post("/")
def post_attachments_list(attachment: Attachment):
    return list_routes.post_attachments(attachment)


# Do not allow to UPDATE entire attachment collection
@router.put("/")
def put_attachments_list():
    return list_routes.put_attachments()


# Do not allow to DELETE entire attachment collection
@router.delete("/")
def delete_attachments_list():
    return list_routes.delete_attachments()


""" Detail Routes """


# Get a single attachment from the database
@router.get("/{attachment_id}")
def get_attachment_detail(attachment_id: str):
    return detail_routes.get_attachment(attachment_id)


# Do not allow to CREATE entire attachment collection
@router.post("/{attachment_id}")
def post_attachment_detail():
    return detail_routes.post_attachment()


# Update a single attachment in the database
@router.put("/{attachment_id}")
def put_attachment_detail(attachment: Attachment):
    return detail_routes.put_attachment(attachment)


# Delete a single attachment from the database
@router.delete("/{attachment_id}")
def delete_attachment_detail(attachment_id: str):
    return detail_routes.delete_attachment(attachment_id)
