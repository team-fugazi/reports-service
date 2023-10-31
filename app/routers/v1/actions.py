from fastapi import APIRouter

from ...models.action import Action
from ...controllers.action_list import ActionList
from ...database.mongodb import database

# Router
router = APIRouter(prefix="/actions", tags=["Actions", "v1"])

# Controllers
list_routes = ActionList(database.actions)


# Controllers added to Routes
@router.get("/")
def get_actions_list():
    return list_routes.get_actions()


@router.post("/")
def post_actions_list(action: Action):
    return list_routes.post_actions(action)


@router.put("/")
def put_actions_list():
    return list_routes.put_actions()


@router.delete("/")
def delete_actions_list():
    return list_routes.delete_actions()
