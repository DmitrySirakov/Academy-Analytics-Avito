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
    BASE_URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(BASE_URL, timeout=10)
    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        weather_report = data["weather"]
        return main["temp"], weather_report[0]["description"]
    else:
        return None, None
