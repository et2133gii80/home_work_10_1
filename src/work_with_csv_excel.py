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

# if __name__ == "__main__":
#    print(get_transactions_csv(abs_file_path))


def read_xlsx(file_path: str) -> list[dict]:
    with pd.ExcelFile(file_path, engine="openpyxl") as excel:
        dataframe = pd.read_excel(excel, dtype=str)

    return dataframe.to_dict("records")


# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла логов относительно текущей директории
rel_excel_file_path = os.path.join(current_dir, "../data/transactions_excel.xlsx")
abs_excel_file_path = os.path.abspath(rel_excel_file_path)

if __name__ == "__main__":
    print(read_xlsx(abs_excel_file_path))
