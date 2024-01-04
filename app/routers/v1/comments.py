from fastapi import APIRouter, status

from ...models.comment import Comment, CommentPartial
from ...controllers.comments.list import CommentList
from ...controllers.comments.detail import CommentDetail
from ...database.mongodb import database, user_database

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
    result_com = list(database.comments.aggregate(pipeline))
    result_rep = list(database.reports.aggregate(pipeline))

    # Create a dictionary to map user IDs to counts
    counts_dict = {}

    # Process results from the comments pipeline
    for comment in result_com:
        user_id = comment["_id"]
        counts_dict.setdefault(user_id, {}).update({"comments": comment["count"]})

    # Process results from the reports pipeline
    for report in result_rep:
        user_id = report["_id"]
        counts_dict.setdefault(user_id, {}).update({"reports": report["count"]})

    # Convert the counts_dict to a list of merged results
    merged_results = [
        {"_id": user_id, **counts} for user_id, counts in counts_dict.items()
    ]

    # TODO: Get user profile from user database
    users = []
    for res in merged_results:
        user = res["_id"]
        users.append(user)

    # Use $in operator to find documents where 'auth0_user_id' is in the list of IDs
    query = {"auth0_user_id": {"$in": users}}

    # Use find() to retrieve all matching documents
    matching_profiles = user_database.profiles.find(query)

    # Iterate over the results
    for profile in matching_profiles:
        print(profile["first_name"])



    # Sort the merged results based on the total count (comments + reports)
    merged_results.sort(
        key=lambda x: x.get("comments", 0) + x.get("reports", 0), reverse=True
    )

    return {
        "status": status.HTTP_200_OK,
        "meta": generate_meta(),
        "data": merged_results,
    }
