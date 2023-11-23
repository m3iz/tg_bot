import asyncio
import json
import requests

from kinopoisk_dev import KinopoiskDev
from kinopoisk_dev.model import Movie

TOKEN = "WK9YDQE-XEMMP4E-M5CK6NV-85WWH6E"

class Film:
    def __init__(self):
        self.__json_data = asyncio.run(get_random_async())
        self.__data_obj = json.loads(self.__json_data.json())
        self.__info = name_value=self.__data_obj.get("name")+" (" + str(self.__data_obj.get("year")) + ")" + " Жанр: " + self.__data_obj.get("genres")[0].get("name") + " Рейтинг: kp: " + str(self.__data_obj.get("rating").get("kp")) + " imdb: " + str(self.__data_obj.get("rating").get("imdb")) + "\n" + self.__data_obj.get("description")
        self.__url_value = self.__data_obj.get("poster")
        self.__image_url = self.__url_value.get("url")
        self.__genre = self.__data_obj.get("genres")[0].get("name")
        self.__description_value = self.__data_obj.get("description")
    def get_poster(self):
        response = requests.get(self.__image_url)

        if response.status_code == 200:
            # Получаем содержимое изображения в бинарном виде
            image_data = response.content
        return image_data
    def get_genre(self):
        return self.__genre
    def get_info(self):
        return self.__info

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

    test = Film()
    print(test.get_info())
    #with open("poster.jpg", 'wb') as file:
    #    file.write(test.get_poster())