import json
import logging
import os
from json import JSONDecodeError
from typing import Any

from src.external_api import conversion

# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла логов относительно текущей директории
rel_log_file_path = os.path.join(current_dir, "../logs/utils.log")
abs_log_file_path = os.path.abspath(rel_log_file_path)

# Создаем путь до файла JSON относительно текущей директории
rel_src_file_path = os.path.join(current_dir, "../data/operations.json")
abs_src_file_path = os.path.abspath(rel_src_file_path)

# Добавляем логгер, который записывает логи в файл.
logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(abs_log_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def transaction_data(transactions: str) -> list:
    try:
        logger.error(f"Проверка корректности, принимаемого на вход путь до JSON-файла{transactions}")
        with open(transactions, encoding="utf-8") as f:
            try:
                data = json.load(f)
            except JSONDecodeError as ex:
                logger.error(f"Произошла ошибка {ex}")
                return []
            logger.info(f"Проверка того яв-ся ли JSON-файл{transactions} списком")
            if not isinstance(data, list):
                return []
        return data
    except FileNotFoundError as ex:
        logger.error(f"Произошла ошибка {ex}")
        return []


def transaction_amount(trans: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    logger.info(f"Проверка валюты{currency} транзакции {trans} ")
    if trans["operationAmount"]["currency"]["code"] == "RUB":
        amount = trans["operationAmount"]["amount"]
        return amount
    else:
        amount = conversion(trans)
        return amount


if __name__ == "__main__":
    json.dumps(transaction_data(abs_src_file_path), indent=4)
    transaction_amount(
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
    )
