import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app.core.config import settings
from app.core.container import Container
from app.api.v1 import routers


def create_app() -> FastAPI:
    fastapi_app = FastAPI(
        title=settings.project_name,
        default_response_class=ORJSONResponse,
    )

    container = Container()
    container.init_resources()
    container.wire(modules=settings.container_wiring_modules)

    fastapi_app.container = container
    fastapi_app.include_router(routers.api_router, prefix=settings.api_v1_prefix)


    return fastapi_app

app = create_app()


if __name__ == '__main__':
    uvicorn.run(app='app.main:app', reload=True)