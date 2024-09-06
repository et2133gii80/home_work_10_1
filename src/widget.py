from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: Union[str]) -> str:
    """Фукнция маскировки карт и счетов"""
    if len(account_card.split()[-1]) == 16:
        new_account_card = get_mask_card_number(account_card.split()[-1])
        result = f"{account_card[:-16]}{new_account_card}"
    elif len(account_card.split()[-1]) == 20:
        new_number = get_mask_account(account_card.split()[-1])
        result = f"{account_card[:-20]}{new_number}"
    else:
        return "Некорректные данные"
    return result


def get_date(date: Union[str]) -> str:
    """Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
    new_date = date[0:10].split("-")
    return ".".join(new_date[::-1])