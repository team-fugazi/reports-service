from typing import List
from fastapi import HTTPException, status

# Models
from ...models.comment import Comment

class CommentList:
    def __init__(self, db):
        self.db = db
    
    # Get all comments from the database
    def get_comments(self) -> List[Comment]:
        comments = self.db.find()
        return [Comment(**comment) for comment in comments]
    
    # Create a new comment in the database
    def post_comments(self, comment: Comment) -> Comment:
        comment_dict = comment.model_dump()
        result = self.db.insert_one(comment_dict)
        return {"status": status.HTTP_201_CREATED, "id": str(result.inserted_id)}
    
    # Do not allow to UPDATE entire comment collection
    def put_comments(self) -> HTTPException:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    # Do not allow to DELETE entire comment collection
    def delete_comments(self) -> HTTPException:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED)