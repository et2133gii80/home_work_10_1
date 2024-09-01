from typing import Union


def get_mask_card_number(card_number: Union[str]) -> str:
    """Функция маскировки номера банковской карты"""
    x = str(card_number)
    return x[:6] + (len(x) - 10) * "*" + x[-4:]


def get_mask_account(account: Union[str]) -> str:
    """Функция маскировки номера банковского счета"""
    s = str(account)
    return "**" + s[-4:]
