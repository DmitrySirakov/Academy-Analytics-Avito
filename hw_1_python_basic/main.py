import streamlit as st
from chat_utils import display_message
from weather_api import get_weather


def main():
    """
    Основная функция для запуска Streamlit приложения.
    """
    st.title("🦆 Утка и её приключения 🗺️")
    display_message(
        "Утка-маляр 🦆 решила выпить зайти в бар. Взять ей зонтик? ☂️", "bot"
    )
    option = st.selectbox("", ["Выберите ответ", "да", "нет"])

    if option == "да":
        display_message("да", "user")
        step2_umbrella()
    elif option == "нет":
        display_message("нет", "user")
        step2_no_umbrella()


def step2_umbrella():
    """
    Обработка выбора "да" и отображение соответствующего сообщения.
    """
    temp, description = get_weather()
    if "дождь" in description:
        display_message(
            f"Сейчас в Москве {temp}°C и {description}. Утка с умом взяла зонтик! ☂️",
            "bot",
        )
    else:
        display_message(
            f"Сейчас в Москве {temp}°C и {description}.\
            Утка решила взять зонтик, чтобы быть готовой к любой погоде! ⛅",
            "bot",
        )


def step2_no_umbrella():
    """
    Обработка выбора "нет" и отображение соответствующего сообщения.
    """
    temp, description = get_weather()
    if "дождь" in description:
        display_message(
            f"Сейчас в Москве {temp}°C и {description}.\
                  Всё-таки пошёл дождь и уточка не намочила крылышки! ☂️",
            "bot",
        )
    else:
        display_message(
            f"Сейчас в Москве {temp}°C и {description}.\
                  Утка не взяла зонтик и наслаждается прекрасным днём! ☀️",
            "bot",
        )


if __name__ == "__main__":
    main()
