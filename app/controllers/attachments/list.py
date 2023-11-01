from typing import List
from fastapi import HTTPException, status

# Models
from ...models.attachment import Attachment


class AttachmentList:
    def __init__(self, db):
        self.db = db

    # Get all attachments from the database
    def get_attachments(self) -> List[Attachment]:
        attachments = self.db.find()
        return [Attachment(**attachment) for attachment in attachments]

    # Create a new attachment in the database
    def post_attachments(self, attachment: Attachment) -> Attachment:
        attachment_dict = attachment.model_dump()
        result = self.db.insert_one(attachment_dict)
        return {"status": status.HTTP_201_CREATED, "id": str(result.inserted_id)}

    # Do not allow to UPDATE entire attachment collection
    def put_attachments(self) -> HTTPException:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail="Bulk update not allowed for attachments",
        )

    # Do not allow to DELETE entire attachment collection
    def delete_attachments(self) -> HTTPException:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail="Bulk delete not allowed for attachments",
        )
