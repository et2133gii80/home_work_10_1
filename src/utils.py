import csv
import json
import logging
import os
from json import JSONDecodeError
from typing import Any

import pandas as pd

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


def transaction_data_csv(csv_path: str) -> list[dict]:
    """Aункция пути до CSV-файла и возвращает список словарей с данными о финансовых транзакциях"""

    transaction_list = []
    try:
        with open(csv_path, encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file, delimiter=";")
            next(reader)
            for row in reader:
                if row:
                    id_, state, date, amount, currency_name, currency_code, from_, to, description = row
                    transaction_list.append(
                        {
                            "id": str(id_),
                            "state": state,
                            "date": date,
                            "operationAmount": {
                                "amount": str(amount),
                                "currency": {"name": currency_name, "code": currency_code},
                            },
                            "description": description,
                            "from": from_,
                            "to": to,
                        }
                    )
    except Exception:
        return []
    return transaction_list


def transaction_data_excel(excel_path: str) -> list[dict]:
    """FAункция пути до EXCEL-файла и возвращает список словарей с данными о финансовых транзакциях"""

    transaction_list = []
    try:
        excel_data = pd.read_excel(excel_path)
        len_, b = excel_data.shape
        for i in range(len_):
            if excel_data["id"][i]:
                transaction_list.append(
                    {
                        "id": str(excel_data["id"][i]),
                        "state": excel_data["state"][i],
                        "date": excel_data["date"][i],
                        "operationAmount": {
                            "amount": str(excel_data["amount"][i]),
                            "currency": {
                                "name": excel_data["currency_name"][i],
                                "code": excel_data["currency_code"][i],
                            },
                        },
                        "description": excel_data["description"][i],
                        "from": excel_data["from"][i],
                        "to": excel_data["to"][i],
                    }
                )
            else:
                continue
    except Exception:
        return []
    return transaction_list
