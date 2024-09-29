from typing import Any


def filter_by_state(list_dict: list[dict[str, Any]], state: str = "EXECUTED") -> Any:
    """Фукнция принимает на вход список словарей и выдает новый список с заданным ключом"""
    new_list = []
    for key in list_dict:
        if key.get("state") == state:
            new_list.append(key)
    return new_list


def sort_by_date(date_list: list, reverse_list: bool = True) -> list | bool:
    sorted_list = sorted(date_list, key=lambda date_dict: date_dict.get("date"), reverse=reverse_list)

    """Функция, которая ринимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание)"""

    return sorted_list
