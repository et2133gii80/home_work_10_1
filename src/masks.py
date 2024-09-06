from typing import Union


def get_mask_card_number(card_number: Union[str]) -> str:
    """Функция маскировки номера банковской карты"""
    if len(card_number) == 16 and card_number.isdigit():
        return card_number[:6] + (len(card_number) - 10) * "*" + card_number[-4:]
    else:
        return "Некорректные данные"


def get_mask_account(account: Union[str]) -> str:
    """Функция маскировки номера банковского счета"""
    if len(account) == 20 and account.isdigit():
        return "**" + account[-4:]
    else:
        return "Некорректные данные"


