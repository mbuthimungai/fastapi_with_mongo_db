from fastapi import FastAPI
from app.core.settings import settings
from app.api.v1.api import api_router
app = FastAPI(
    title=settings.API_TITLE
)
app.include_router(api_router, prefix="/api/v1")