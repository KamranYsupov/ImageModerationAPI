from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Настройки API"""

    project_name: str = Field(title='Название проекта')
    api_v1_prefix: str = Field(title='Префикс первой версии API', default='/api/v1')

    # region OpenAI
    deepai_base_url: str = Field(
        title='DeepAI base url',
        default='https://api.deepai.com/api/',
    )
    deepai_api_key: str = Field(title='DeepAI Api ключ')
    # endregion

    container_wiring_modules: list = [
        'app.api.v1.endpoints'
    ]


    class Config:
        env_file = '.env'


settings = Settings()