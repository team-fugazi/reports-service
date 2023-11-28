from fastapi import APIRouter

from ...models.action import Action
from ...controllers.actions.list import ActionList
from ...controllers.actions.detail import ActionDetail
from ...database.mongodb import database

# Router
router = APIRouter(prefix="/actions", tags=["Actions"])

# Controllers
list_routes = ActionList(database.actions)
detail_routes = ActionDetail(database.actions)


# Controllers added to Routes
@router.get("/")
def get_actions_list():
    return list_routes.get_actions()


# Detail Routes
@router.get("/{action_id}")
def get_actions_detail(action_id: str):
    return detail_routes.get_action(action_id)


@router.put("/{action_id}")
def put_actions_detail(action_id: str, action: Action):
    return detail_routes.put_action(action_id, action)
