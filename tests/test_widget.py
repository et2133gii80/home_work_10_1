from typing import Any

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_card, mask_number_card",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 700079******6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("adcdgfedhssterjjyth", "Некорректные данные"),
        ("1234adcsd", "Некорректные данные"),
    ],
)
def test_mask_account_card(account_card: Any, mask_number_card: Any) -> Any:
    assert mask_account_card(account_card) == mask_number_card


@pytest.mark.parametrize("date, new_date", [("2024-03-11T02:26:18.671407", "11.03.2024")])
def test_get_date(date: Any, new_date: Any) -> Any:
    assert get_date(date) == new_date
