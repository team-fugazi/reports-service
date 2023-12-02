from typing import List
from fastapi import HTTPException, status
from pymongo.collection import Collection
from datetime import datetime

# Models
from ...models.comment import CommentPartial, Comment

# Helpers
from ...helpers.meta_generator import generate_meta


class CommentList:
    def __init__(self, db: Collection):
        self.db = db

    # Get all comments from the database
    def get_comments(self) -> List[Comment]:
        comments = self.db.find()

        # get document count
        num_documents = self.db.count_documents({})

        # modify metadata to include return count
        modified_meta = generate_meta()
        modified_meta["total_count"] = num_documents

        return {
            "status": status.HTTP_200_OK,
            "meta": modified_meta,
            "data": [Comment(**comment) for comment in comments],
        }

    # Create a new comment in the database
    def post_comments(self, comment_partial: CommentPartial) -> Comment:
        # Convert partial response body to dict
        comment_dict = comment_partial.model_dump()

        # Add metadata
        comment_dict["id"] = None
        comment_dict["created_at"] = datetime.now()
        comment_dict["updated_at"] = None
        comment_dict["deleted_at"] = None

        # Validate and create a Comment instance
        comment_full = Comment(**comment_dict)

        # Insert comment into the database
        result = self.db.insert_one(
            comment_full.model_dump(by_alias=True, exclude=["id"])
        )

        # Check if comment was created
        if not result.acknowledged:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Comment could not be created",
            )

        return {
            "status": status.HTTP_201_CREATED,
            "meta": generate_meta(),
            "message": "Comment created successfully",
            "data": Comment(**comment_dict),
        }

    # Do not allow to UPDATE entire comment collection
    def put_comments(self) -> HTTPException:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED)

    # Do not allow to DELETE entire comment collection
    def delete_comments(self) -> HTTPException:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED)
