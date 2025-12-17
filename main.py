import os
from typing import Dict, Any

from fastapi import FastAPI, Request
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.cors import CORSMiddleware

from apps.api import api_router
from apps.swagger.i18n import PLACEHOLDER_PREFIX, tags_metadata, i18n_list
from apps.swagger.i18n import get_translation, DEFAULT_LANG


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan,
    docs_url=None,
    redoc_url=None,
)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)