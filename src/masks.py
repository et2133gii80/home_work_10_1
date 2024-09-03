from typing import Union


def get_mask_card_number(card_number: Union[str]) -> str:
    """Функция маскировки номера банковской карты"""
    return card_number[:6] + (len(card_number) - 10) * "*" + card_number[-4:]


def get_mask_account(account: Union[str]) -> str:
    """Функция маскировки номера банковского счета"""
    return "**" + account[-4:]