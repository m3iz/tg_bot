import asyncio
import json
import requests

from kinopoisk_dev import KinopoiskDev
from kinopoisk_dev.model import Movie

TOKEN = "WK9YDQE-XEMMP4E-M5CK6NV-85WWH6E"


async def get_random_async() -> Movie:
    """
    Асинхронный запрос.
    Получить рандомный фильм
    :return: Информация о фильме
    """
    kp = KinopoiskDev(token=TOKEN)
    return await kp.arandom()


def get_random() -> Movie:
    """
    Синхронный запрос.
    Получить рандомный фильм
    :return: Информация о фильме
    """
    kp = KinopoiskDev(token=TOKEN)
    return kp.random()


if __name__ == "__main__":
    adata = asyncio.run(get_random_async())
    data = get_random()

    # Распарсим строку JSON в объект Python

    data_obj = json.loads(data.json())
    print(data_obj)
    name_value=data_obj.get("name")+" (" + data_obj.get("")
    print(name_value)
    # Получим значение поля "description"
    url_value = data_obj.get("poster")
    image_url=url_value.get("url")
    description_value = data_obj.get("description")
    # Выведем значение на экран
    print(description_value)

    response = requests.get(image_url)

    if response.status_code == 200:
        # Получаем содержимое изображения в бинарном виде
        image_data = response.content

        with open("poster.jpg", 'wb') as file:
            # Записываем данные изображения в файл
            file.write(image_data)