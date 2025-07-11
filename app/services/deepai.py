from io import BufferedReader

import aiohttp

from app.core.config import settings


class DeepAIService:
    def __init__(
            self,
            base_url: str = settings.deepai_base_url,
            api_key: str = settings.deepai_api_key,
    ):
        self.base_url = base_url
        self.__api_key = api_key


    async def get_nsfw_image_score(
            self,
            image: bytes,
            content_type: str
    ):
        url = f'{self.base_url}nsfw-detector'
        print(url)
        headers = {'api-key': self.__api_key}

        async with aiohttp.ClientSession() as session:
            form_data = aiohttp.FormData()
            form_data.add_field('image', image, content_type=content_type)

            async with session.post(
                    url,
                    data=form_data,
                    headers=headers
            ) as response:
                result = await response.json()
                print(result)
                return result.get('output', {}).get('nsfw_score', 0)
