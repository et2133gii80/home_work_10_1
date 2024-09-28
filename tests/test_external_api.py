from typing import Any
from unittest.mock import patch

import pytest

from src.external_api import conversion


@pytest.fixture
def trans_3() -> Any:
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@patch("requests.get")
def test_conversion(mock_get: Any, trans_3: Any) -> Any:
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1724671757, "rate": 91.475458},
        "date": "2024-08-26",
        "result": 752053.586137,
    }
    assert conversion(trans_3) == 752053.586137
