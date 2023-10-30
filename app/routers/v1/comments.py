from fastapi import APIRouter

from ...models.comment import Comment
from ...controllers.comment_list import CommentList
from ...database.mongodb import database

# Router
router = APIRouter(prefix="/reports", tags=["Reports"])