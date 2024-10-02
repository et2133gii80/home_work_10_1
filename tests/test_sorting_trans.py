from unittest.mock import patch

import pytest

from src.sorting_transactions import counting_categorys, sorting_transactions_by_description

data = [
    {
        "id": 650703.0,
        "description": "Перевод организации",
    },
    {
        "id": 3598919.0,
        "description": "Перевод с карты на карту",
    },
    {
        "id": 650703.0,
        "description": "Перевод организации",
    },
    {
        "id": 3598919.0,
        "description": "Перевод с карты на карту",
    },
    {
        "id": 650703.0,
        "description": "Перевод организации",
    },
    {
        "id": 3598919.0,
        "description": "Перевод с карты на карту",
    },
    {
        "id": 650703.0,
        "description": "Перевод организации",
    },
    {
        "id": 3598919.0,
        "description": "Перевод с карты на карту",
    },
]


@pytest.mark.parametrize(
    "data, categories, expected",
    [
        (data, ["перевод с карты", "перевод Организац"], {"Перевод организации": 4, "Перевод с карты на карту": 4}),
        (data, ["перевод с карты"], {"Перевод с карты на карту": 4}),
        (data, [], {}),
        ([], ["перевод с карты", "перевод Организац"], {}),
    ],
)
def test_counting_categorys(data, categories, expected):
    assert counting_categorys(data, categories) == expected


data1 = [
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


@pytest.fixture
def trans1():
    return data1


@patch("src.sorting_transactions")
def test_sorting_transactions_by_description(mock_currency, trans1):
    mock_currency.return_value == [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        }
    ]
    assert sorting_transactions_by_description(trans1, "Счет 41421565395219882431")
