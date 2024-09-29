import logging
import os
from typing import Union

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rel_file_path)

# Добавляем логгер, который записывает логи в файл.
logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(abs_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str]) -> str:
    """Функция маскировки номера банковской карты"""
    logger.info(f"Проверка корректности вводимых данных номера карты{card_number}")
    if len(card_number) == 16 and card_number.isdigit():
        return card_number[:6] + (len(card_number) - 10) * "*" + card_number[-4:]
    else:
        return "Некорректные данные"


def get_mask_account(account: Union[str]) -> str:
    """Функция маскировки номера банковского счета"""
    logger.info(f"Проверка корректности вводимых данных счета {account}")
    if len(account) == 20 and account.isdigit():
        return "**" + account[-4:]
    else:
        return "Некорректные данные"


if __name__ == "__main__":
    get_mask_card_number("7000792289606361")
    get_mask_account("73654108430135874305")
