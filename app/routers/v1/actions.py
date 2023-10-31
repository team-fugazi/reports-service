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


@router.post("/")
def post_actions_list(action: Action):
    return list_routes.post_actions(action)


@router.put("/")
def put_actions_list():
    return list_routes.put_actions()


@router.delete("/")
def delete_actions_list():
    return list_routes.delete_actions()


# Detail Routes
@router.get("/{action_id}")
def get_actions_detail(action_id: str):
    return detail_routes.get_action(action_id)


@router.post("/{action_id}")
def post_actions_detail(action_id: str, action: Action):
    return detail_routes.post_action(action_id, action)


@router.put("/{action_id}")
def put_actions_detail(action_id: str, action: Action):
    return detail_routes.put_action(action_id, action)


@router.delete("/{action_id}")
def delete_actions_detail(action_id: str):
    return detail_routes.delete_action(action_id)
