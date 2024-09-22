import json
from json import JSONDecodeError
from typing import Any
from src.external_api import conversion


def transaction_data(transactions: str) -> list:
    try:
        with open(transactions, encoding="utf-8") as f:
            try:
                data = json.load(f)
            except JSONDecodeError:
                return []
            if not isinstance(data, list):
                return []
        return data
    except FileNotFoundError:
        return []


def transaction_amount(trans: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if trans["operationAmount"]["currency"]["code"] == "RUB":
        amount = trans["operationAmount"]["amount"]
        return amount
    else:
        amount = conversion(trans)
        return amount
