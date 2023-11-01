# Path: app/controllers/comments/detail.py

from fastapi import HTTPException, status
from bson import ObjectId

# Models
from ...models.comment import Comment

# Transformers
from ...helpers.transformers import transform_mongodb_to_comment


class CommentDetail:
    def __init__(self, db):
        self.db = db

    # Get a single comment from the database
    def get_comment(self, comment_id: str) -> Comment:
        comment = self.db.find_one({"_id": ObjectId(comment_id)})

        if not comment:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Comment with id {comment_id} not found",
            )

        return transform_mongodb_to_comment(comment)
    
    # Do not allow to CREATE entire comment collection
    def post_comment(self) -> HTTPException:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail="Use PUT method to update comments",
        )
    
    # Update a single comment in the database
    def put_comment(self, comment: Comment) -> Comment:
        comment_dict = comment.model_dump()
        print(comment_dict)

        result = self.db.update_one(
            {"_id": ObjectId(comment.comment_id)}, {"$set": comment_dict}
        )

        if result.modified_count == 1:
            return {
                "status": status.HTTP_200_OK,
                "detail": "Comment updated successfully",
            }
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Comment with id {comment.comment_id} not found",
            )
        
    # Delete a single comment from the database
    def delete_comment(self, comment_id: str):
        result = self.db.delete_one({"_id": ObjectId(comment_id)})
        if result.deleted_count == 1:
            return {
                "status": status.HTTP_200_OK,
                "detail": "Comment deleted successfully",
            }
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Comment with id {comment_id} not found",
            )
