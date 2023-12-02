from fastapi import APIRouter, status

from ...models.comment import Comment, CommentPartial
from ...controllers.comments.list import CommentList
from ...controllers.comments.detail import CommentDetail
from ...database.mongodb import database

# utils
from ...helpers.meta_generator import generate_meta

# Router
router = APIRouter(prefix="/comments", tags=["Comments"])

# Initialize controller
comment_list = CommentList(database.comments)
comment_detail = CommentDetail(database.comments)


# Get all comments
@router.get("/")
def get_comments():
    return comment_list.get_comments()


# Get a single comment
@router.get("/{comment_id}")
def get_comment(comment_id: str):
    return comment_detail.get_comment(comment_id)


# Update a single comment
@router.put("/{comment_id}")
def put_comment(comment: Comment):
    return comment_detail.put_comment(comment)


""" Special Routes """


@router.get("/active/comments")
def get_active_comments(limit: int = 1):
    # Aggregation pipeline
    pipeline = [
        {"$group": {"_id": "$user", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": limit},
    ]

    # Execute aggregation pipeline
    result = list(database.comments.aggregate(pipeline))

    return {
            "status": status.HTTP_200_OK,
            "meta": generate_meta(),
            "data": result,
        }
