from dependency_injector import containers, providers

from app.services.deepai import DeepAIService


class Container(containers.DeclarativeContainer):
    deepai_service = providers.Factory(DeepAIService)