from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: Union[str]) -> str:
    """Фукнция маскировки карт и счетов"""
    parts = account_card.split()  # делим на части по пробелу
    number = parts[-1]  # забираем последний элемент (там всегда номер карты или счёта)
    if account_card.lower().startswith("счет"):  # если пришёл счёт - отдаём номер в ф-цию маскировки номера счёта
        hidden_number = get_mask_account(number)
    else:  # иначе отдаём номер в функцию маскироки карты и получаем скрытый вариант номера
        hidden_number = get_mask_card_number(number)
    parts[-1] = hidden_number  # подставляем скрытый номер обратно
    return " ".join(parts)  # соединяем список в строку


def get_date(date: Union[str]) -> str:
    """Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
    new_date = date[0:10].split("-")
    return ".".join(new_date[::-1])
