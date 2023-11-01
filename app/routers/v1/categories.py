# Path: app/routers/v1/categories.py
from fastapi import APIRouter

from ...models.category import Category
from ...controllers.categories.list import CategoryList
from ...controllers.categories.detail import CategoryDetail
from ...database.mongodb import database

# Router
router = APIRouter(prefix="/categories", tags=["Categories"])

# Initialize controller
category_list = CategoryList(database.categories)
category_detail = CategoryDetail(database.categories)


# Get all categories
@router.get("/")
def get_categories():
    return category_list.get_categories()


# Create a new category
@router.post("/")
def post_categories(category: Category):
    return category_list.post_categories(category)


# Do not allow to UPDATE entire category collection
@router.put("/")
def put_categories():
    return category_list.put_categories()


# Do not allow to DELETE entire category collection
@router.delete("/")
def delete_categories():
    return category_list.delete_categories()


# Get a single category
@router.get("/{category_id}")
def get_category_detail(category_id: str):
    return category_detail.get_category(category_id)


# Do not allow to CREATE entire category collection
@router.post("/{category_id}")
def post_category_detail():
    return category_detail.post_category()


# Update a single category
@router.put("/{category_id}")
def put_category_detail(category_id: str, category: Category):
    category.category_id = category_id
    return category_detail.put_category(category)


# Delete a single category
@router.delete("/{category_id}")
def delete_category_detail(category_id: str):
    return category_detail.delete_category(category_id)
