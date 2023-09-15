import streamlit as st


def display_message(message: str, sender="user") -> None:
    """
    Отображает сообщение в чате.

    Parameters
    ----------
    message : str
        Текст сообщения.
    sender : str, optional
        Отправитель сообщения ("user" или "bot"). По умолчанию "user".

    Returns
    -------
    None
    """
    if sender == "user":
        st.markdown(
            f"<div style='text-align: left; border: 1px solid gray; padding: 10px; margin: 5px;\
                  border-radius: 5px;'>{message}</div>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"<div style='text-align: right; border: 1px solid green; padding: 10px; margin: 5px;\
                  border-radius: 5px;'>{message}</div>",
            unsafe_allow_html=True,
        )
