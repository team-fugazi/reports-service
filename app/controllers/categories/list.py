from typing import List
from fastapi import HTTPException, status

# Models
from ...models.category import Category


class CategoryList:
    def __init__(self, db):
        self.db = db

    # Get all categories from the database
    def get_categories(self) -> List[Category]:
        categories = self.db.find()
        return [Category(**category) for category in categories]

    # Create a new category in the database
    def post_categories(self, category: Category) -> Category:
        category_dict = category.model_dump()
        result = self.db.insert_one(category_dict)
        return {"status": status.HTTP_201_CREATED, "id": str(result.inserted_id)}

    # Do not allow to UPDATE entire category collection
    def put_categories(self) -> HTTPException:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail="Bulk update not allowed for categories",
        )

    # Do not allow to DELETE entire category collection
    def delete_categories(self) -> HTTPException:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail="Bulk delete not allowed for categories",
        )
