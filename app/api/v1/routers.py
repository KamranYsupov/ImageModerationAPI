from fastapi import APIRouter

from app.api.v1.endpoints.moderate import router as moderate_router

api_router = APIRouter()

api_router.include_router(moderate_router)