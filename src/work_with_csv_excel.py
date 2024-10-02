import csv
import os
from typing import Any

import pandas as pd


def get_transactions_csv(file_path: str) -> list[dict[Any, Any]]:
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        result = []
        try:
            try:
                for row in reader:
                    row_dict = {
                        "id": row["id"],
                        "state": row["state"],
                        "date": row["date"],
                        "operationAmount": {
                            "amount": row["amount"],
                            "currency": {"name": row["currency_name"], "code": row["currency_code"]},
                        },
                        "description": row["description"],
                        "from": row["from"],
                        "to": row["to"],
                    }
                    result.append(row_dict)
            except AssertionError:
                return []
        except FileNotFoundError:
            return []
    return result


# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла логов относительно текущей директории
rel_csv_file_path = os.path.join(current_dir, "../data/transactions.csv")
abs_file_path = os.path.abspath(rel_csv_file_path)

if __name__ == "__main__":
    print(get_transactions_csv(abs_file_path))


def read_xlsx(file_path: str) -> list[dict]:
    transaction_list = []
    try:
        excel_data = pd.read_excel(file_path)
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


# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла логов относительно текущей директории
rel_excel_file_path = os.path.join(current_dir, "../data/transactions_excel.xlsx")
abs_excel_file_path = os.path.abspath(rel_excel_file_path)

if __name__ == "__main__":
    print(read_xlsx(abs_excel_file_path))
