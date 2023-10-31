from fastapi import APIRouter

from ...models.category import Category
from ...controllers.categories.list import CategoryList
from ...database.mongodb import database

# Router
router = APIRouter(prefix="/categories", tags=["Categories"])

# Initialize controller
category_list = CategoryList(database.categories)

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