from typing import Any


def filter_by_state(list_dict: list[dict[str, Any]], state: str = "EXECUTED") -> Any:
    """Фукнция принимает на вход список словарей и выдает новый список с заданным ключом"""
    new_list = []
    for key in list_dict:
        if key.get("state") == state:
            new_list.append(key)
    return new_list


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """
    Функция принимает на вход список словарей и возвращает новый список, в котором исходные
    словари отсортированы по убыванию даты
    """
    operations = sorted(operations, key=lambda new_list_of_dict: new_list_of_dict["date"], reverse=reverse)
    return operations
