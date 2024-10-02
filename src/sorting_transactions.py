import re
from collections import Counter
from typing import Dict, List

data = [
    {
        "id": 716496732,
        "state": "EXECUTED",
        "date": "2018-04-04T17:33:34.701093",
        "operationAmount": {"amount": "40701.91", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Visa Gold 5999414228426353",
        "to": "Счет 72731966109147704472",
    },
    {
        "id": 863064926,
        "state": "EXECUTED",
        "date": "2019-12-08T22:46:21.935582",
        "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}},
        "description": "Открытие вклада",
        "to": "Счет 90424923579946435907",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431",
    },
]


def sorting_transactions_by_description(transactions: list[dict], input_user: str) -> list[dict]:
    """Функция принимает список транзакций (словарей) и слово для сортировки.
    Возвращает список транзакций (словарей), у которых в описании есть указанное слово."""
    new_list = []
    for i in transactions:
        if "from" not in i.keys() or i["from"] == "nan":
            if i["description"] == "Открытие вклада":
                if re.search(input_user, str(i["description"])):
                    new_list.append(i)
                elif re.search(input_user, str(i["to"])):
                    new_list.append(i)
        if "from" in i.keys():
            if re.search(input_user, str(i["from"])):
                new_list.append(i)
            elif re.search(input_user, str(i["to"])):
                new_list.append(i)

    return new_list


if __name__ == "__main__":
    print(sorting_transactions_by_description(data, "Счет 41421565395219882431"))


def counting_categorys(transactions: List[Dict], categories: List[str]) -> Dict:
    """Функция принимает список транзакций (словарей) и категории (список).
    Возвращает словарь вида категория: количество операций."""
    category_list = []
    for transaction in transactions:
        for category in categories:
            pattern = rf"{category}"
            if re.findall(pattern, transaction["description"], flags=re.IGNORECASE):
                category_list.append(transaction["description"])
    result_category_dict = Counter(category_list)
    return dict(result_category_dict)
