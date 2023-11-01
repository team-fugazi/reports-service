# Models
from ..models.action import Action
from ..models.attachment import Attachment
from ..models.category import Category
from ..models.comment import Comment
from ..models.report import Report


# Transforms a MongoDB document into an Action model TODO: convert fields
def transform_mongodb_to_action(document):
    action_id = str(document.get("_id", ""))
    return Action(
        id=action_id,
        action_id=document.get("action_id", ""),
        name=document.get("name", ""),
        description=document.get("description", ""),
    )


# Transforms a MongoDB document into an Attachment model TODO: convert fields
def transform_mongodb_to_attachment(document):
    attachment_id = str(document.get("_id", ""))
    return Attachment(
        id=attachment_id,
        attachment_id=document.get("attachment_id", ""),
        name=document.get("name", ""),
        description=document.get("description", ""),
    )


# Transforms a MongoDB document into a Category model
def transform_mongodb_to_category(document):
    category_id = str(document.get("_id", ""))
    return Category(
        id=category_id,
        category_id=document.get("category_id", ""),
        name=document.get("name", ""),
        description=document.get("description", ""),
    )


# Transforms a MongoDB document into a Comment model TODO: convert fields
def transform_mongodb_to_comment(document):
    comment_id = str(document.get("_id", ""))
    return Comment(
        id=comment_id,
        comment_id=document.get("comment_id", ""),
        name=document.get("name", ""),
        description=document.get("description", ""),
    )


# Transforms a MongoDB document into a Report model TODO: convert fields
def transform_mongodb_to_report(document):
    report_id = str(document.get("_id", ""))
    return Report(
        id=report_id,
        report_id=document.get("report_id", ""),
        name=document.get("name", ""),
        description=document.get("description", ""),
    )
