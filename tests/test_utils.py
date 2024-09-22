from unittest.mock import patch

import os

import pytest

from src.utils import transaction_data, transaction_amount


@pytest.fixture
def empty_jsonfile():
    return ""


def test_transaction_data_empty_jsonfile(empty_jsonfile):
    assert transaction_data(empty_jsonfile) == []


@pytest.fixture
def transactions():
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    return PATH_TO_FILE


def test_transaction_data_correctness_function(transactions):
    assert transaction_data(transactions)[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def not_list():
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations1.json")
    return PATH_TO_FILE


def test_transaction_data_not_list(not_list):
    assert transaction_data(not_list) == []


@pytest.fixture
def path_mistake_json():
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations2.json")
    return PATH_TO_FILE


def test_transaction_data_path_mistake_json(path_mistake_json):
    assert transaction_data(path_mistake_json) == []


@pytest.fixture
def trans_1():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@patch("src.utils.conversion")
def test__transaction_amount_non_rub(mock_currency, trans_1):
    mock_currency.return_value = 1000.0
    assert transaction_amount(trans_1) == 1000.0


@pytest.fixture
def trans_2():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@patch("src.utils.transaction_data")
def test_transaction_amount_rub(mock_currency, trans_2):
    mock_currency.return_value = "31957.58"
    assert transaction_amount(trans_2) == "31957.58"
