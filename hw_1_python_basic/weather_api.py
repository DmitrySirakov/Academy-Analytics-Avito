import os
import typing
import requests
from dotenv import load_dotenv


def get_weather(city="Moscow") -> typing.Tuple:
    """
    Получает погодные данные для указанного города.

    Parameters
    ----------
    city : str, optional
        Название города. По умолчанию "Moscow".

    Returns
    -------
    tuple
        Кортеж, содержащий температуру и описание погоды.
    """
    load_dotenv()
    API_KEY = os.environ.get("API_KEY")
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather/"
    params = {"q": city, "appid": API_KEY, "units": "metric", "lang": "ru"}
    response = requests.get(BASE_URL, params=params, timeout=10)
    if response.status_code == 200:
        data = response.json()
        return data["main"]["temp"], data["weather"][0]["description"]
    else:
        return None, None
