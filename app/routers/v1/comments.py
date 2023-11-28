from fastapi import APIRouter

from ...models.comment import Comment, CommentPartial
from ...controllers.comments.list import CommentList
from ...controllers.comments.detail import CommentDetail
from ...database.mongodb import database

# Router
router = APIRouter(prefix="/comments", tags=["Comments"])

# Initialize controller
comment_list = CommentList(database.comments)
comment_detail = CommentDetail(database.comments)


# Get all comments
@router.get("/")
def get_comments():
    return comment_list.get_comments()


# Create a new comment
# @router.post("/")
# def post_comments(comment: CommentPartial):
#     return comment_list.post_comments(comment)


# Do not allow to UPDATE entire comment collection
# @router.put("/")
# def put_comments():
#     return comment_list.put_comments()


# Do not allow to DELETE entire comment collection
# @router.delete("/")
# def delete_comments():
#     return comment_list.delete_comments()

# Get a single comment
@router.get("/{comment_id}")
def get_comment(comment_id: str):
    return comment_detail.get_comment(comment_id)

# Do not allow to CREATE entire comment collection
# @router.post("/{comment_id}")
# def post_comment():
#     return comment_detail.post_comment()

# Update a single comment
@router.put("/{comment_id}")
def put_comment(comment: Comment):
    return comment_detail.put_comment(comment)

# Delete a single comment
# @router.delete("/{comment_id}")
# def delete_comment(comment_id: str):
#     return comment_detail.delete_comment(comment_id)
