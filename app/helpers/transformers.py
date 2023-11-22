# Path: tests/helpers/transformers.py

# Models
from ..models.action import Action
from ..models.category import Category
from ..models.comment import Comment
from ..models.report import Report, ReportPartial


# Transforms a MongoDB document into an Action model
def transform_mongodb_to_action(document) -> Action:
    action_id = str(document.get("_id", ""))
    return Action(
        id=action_id,
        action_type=document.get("action_type", ""),
        user_id=document.get("user_id", ""),
        moderator_id=document.get("moderator_id", ""),
        reason=document.get("reason", ""),
        details=document.get("details", ""),
        created_at=document.get("created_at", ""),
        expires_at=document.get("expires_at", ""),
    )


# Transforms a MongoDB document into an Attachment model TODO: convert fields
# def transform_mongodb_to_attachment(document) -> Attachment:
#     attachment_id = str(document.get("_id", ""))
#     return Attachment(
#         id=attachment_id,
#         attachment_id=document.get("attachment_id", ""),
#         name=document.get("name", ""),
#         description=document.get("description", ""),
#    )


# Transforms a MongoDB document into a Category model
def transform_mongodb_to_category(document) -> Category:
    category_id = str(document.get("_id", ""))
    return Category(
        id=category_id,
        category_id=document.get("category_id", ""),
        name=document.get("name", ""),
        description=document.get("description", ""),
    )


# Transforms a MongoDB document into a Comment model TODO: convert fields
def transform_mongodb_to_comment(document) -> Comment:
    comment_id = str(document.get("_id", ""))
    return Comment(
        id=comment_id,
        comment_id=document.get("comment_id", ""),
        name=document.get("name", ""),
        description=document.get("description", ""),
    )


# Transforms a MongoDB document into a Report model TODO: convert fields
def transform_mongodb_to_report(document) -> Report:
    report_id = str(document.get("_id", ""))
    return Report(
        id=report_id,
        report_id=document.get("report_id", ""),
        name=document.get("name", ""),
        description=document.get("description", ""),
    )
