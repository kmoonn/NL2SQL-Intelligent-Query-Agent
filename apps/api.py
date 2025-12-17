from fastapi import APIRouter

from apps.chat.api import chat
from apps.datasource.api import datasource, table_relation, recommended_problem
from apps.system.api import login, user, aimodel, workspace, assistant, parameter
from apps.terminology.api import terminology
from apps.settings.api import base

api_router = APIRouter()
api_router.include_router(login.router)