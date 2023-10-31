from fastapi import APIRouter

from ...models.comment import Comment
from ...controllers.comments.list import CommentList
from ...database.mongodb import database

# Router
router = APIRouter(prefix="/comments", tags=["Comments"])

# Initialize controller
comment_list = CommentList(database.comments)


# Get all comments
@router.get("/")
def get_comments():
    return comment_list.get_comments()


# Create a new comment
@router.post("/")
def post_comments(comment: Comment):
    return comment_list.post_comments(comment)


# Do not allow to UPDATE entire comment collection
@router.put("/")
def put_comments():
    return comment_list.put_comments()


# Do not allow to DELETE entire comment collection
@router.delete("/")
def delete_comments():
    return comment_list.delete_comments()
