from dependency_injector.wiring import inject, Provide
from fastapi import (
    FastAPI,
    Depends,
    UploadFile,
    HTTPException,
    status, APIRouter,
)
import mimetypes

from fastapi import Depends

from app.core.config import settings
from app.core.container import Container
from app.services.deepai import DeepAIService


router = APIRouter()

@router.post('/moderate')
@inject
async def moderate_image(
        file: UploadFile,
        deepai_service: DeepAIService = Depends(
            Provide[Container.deepai_service]
        )
):
    # Проверка типа файла
    content_type = mimetypes.guess_type(file.filename)[0]
    if content_type not in settings.allowed_image_mime_types:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Invalid file type. Only JPG/PNG allowed.'        )

    nsfw_score = await deepai_service.get_nsfw_image_score(
        image=await file.read(),
        content_type=content_type,
    )

    if nsfw_score > 0.7:
        return {'status': 'REJECTED', 'reason': 'NSFW content'}
    return {'status': 'OK'}