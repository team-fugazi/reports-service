# Path: app/controllers/attachments/detail.py

from fastapi import HTTPException, status
from bson import ObjectId

# Models
from ...models.attachment import Attachment

# Transformers
from ...helpers.transformers import transform_mongodb_to_attachment

class AttachmentDetail:
    def __init__(self, db):
        self.db = db

    # Get a single attachment from the database
    def get_attachment(self, attachment_id: str) -> Attachment:
        attachment = self.db.find_one({"_id": ObjectId(attachment_id)})

        if not attachment:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Attachment with id {attachment_id} not found",
            )

        return transform_mongodb_to_attachment(attachment)
    
    # Do not allow to CREATE entire attachment collection
    def post_attachment(self) -> HTTPException:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail="Use PUT method to update attachments",
        )
    
    # Update a single attachment in the database
    def put_attachment(self, attachment: Attachment) -> Attachment:
        attachment_dict = attachment.model_dump()
        print(attachment_dict)

        result = self.db.update_one(
            {"_id": ObjectId(attachment.attachment_id)}, {"$set": attachment_dict}
        )

        if result.modified_count == 1:
            return {
                "status": status.HTTP_200_OK,
                "detail": "Attachment updated successfully",
            }
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Attachment with id {attachment.attachment_id} not found",
            )
        
    # Delete a single attachment from the database
    def delete_attachment(self, attachment_id: str):
        result = self.db.delete_one({"_id": ObjectId(attachment_id)})
        if result.deleted_count == 1:
            return {
                "status": status.HTTP_200_OK,
                "detail": "Attachment deleted successfully",
            }
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Attachment with id {attachment_id} not found",
            )