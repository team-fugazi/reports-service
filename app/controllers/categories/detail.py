from typing import List
from fastapi import HTTPException, status
from bson import ObjectId

# Models
from ...models.category import Category


class CategoryDetail:
    def __init__(self, db):
        self.db = db

    # Get a single category from the database
    def get_category(self, category_id: str) -> Category:
        category = self.db.find_one({"_id": ObjectId(category_id)})

        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Category with id {category_id} not found",
            )

        return Category(**category)

    # Do not allow to CREATE entire category collection
    def post_category(self) -> HTTPException:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail="Method not allowed for creating categories",
        )

    # Update a single category in the database
    def put_category(self, category: Category) -> Category:
        category_dict = category.model_dump()
        result = self.db.update_one(
            {"_id": ObjectId(category.category_id)}, {"$set": category_dict}
        )
        if result.modified_count == 1:
            return {"status": status.HTTP_200_OK}
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Category with id {category.category_id} not found",
            )

    # Delete a single category from the database
    def delete_category(self, category_id: str):
        result = self.db.delete_one({"_id": ObjectId(category_id)})
        if result.deleted_count == 1:
            return {"status": status.HTTP_200_OK}
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Category with id {category_id} not found",
            )
