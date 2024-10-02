import os
from typing import Any
from unittest.mock import patch

import pytest

from src.work_with_csv_excel import get_transactions_csv, read_xlsx


@pytest.fixture
def file_csv() -> Any:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    rel_file_csv = os.path.join(current_dir, "../data/transactions.csv")
    abs_file_csv = os.path.abspath(rel_file_csv)
    return abs_file_csv


@patch("src.work_with_csv_excel.get_transactions_csv")
def test_get_transactions_csv(mock_value: Any, file_csv: Any) -> Any:
    mock_value.return_value = {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "operationAmount": {"amount": "16210", "currency": {"name": "Sol", "code": "PEN"}},
        "description": "Перевод организации",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
    }
    assert get_transactions_csv(file_csv)[0] == {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "operationAmount": {"amount": "16210", "currency": {"name": "Sol", "code": "PEN"}},
        "description": "Перевод организации",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
    }


@pytest.fixture
def file_excel() -> Any:
    current_dir_1 = os.path.dirname(os.path.abspath(__file__))
    rel_file_excel = os.path.join(current_dir_1, "../data/transactions_excel.xlsx")
    abs_file_excel = os.path.abspath(rel_file_excel)
    return abs_file_excel


@patch("src.work_with_csv_excel.read_xlsx")
def test_read_xlsx(mock_value: Any, file_excel: Any) -> Any:
    mock_value.return_value = {
        "id": "4699552.0",
        "state": "EXECUTED",
        "date": "2022-03-23T08:29:37Z",
        "operationAmount": {"amount": "23423.0", "currency": {"name": "Peso", "code": "PHP"}},
        "description": "Перевод с карты на карту",
        "from": "Discover 7269000803370165",
        "to": "American Express 1963030970727681",
    }
    assert read_xlsx(file_excel)[-1] == {
        "id": "4699552.0",
        "state": "EXECUTED",
        "date": "2022-03-23T08:29:37Z",
        "operationAmount": {"amount": "23423.0", "currency": {"name": "Peso", "code": "PHP"}},
        "description": "Перевод с карты на карту",
        "from": "Discover 7269000803370165",
        "to": "American Express 1963030970727681",
    }
