from typing import Any

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, mask_number",
    [
        ("7000792289606361", "700079******6361"),
        ("", "Некорректные данные"),
        ("adcdgfedhssterjjyth", "Некорректные данные"),
        ("1234adcsd", "Некорректные данные"),
    ],
)
def test_get_mask_card_number(card_number: Any, mask_number: Any) -> Any:
    """Тестирование маскировки номера карты"""
    assert get_mask_card_number(card_number) == mask_number


@pytest.mark.parametrize(
    "account, mask_account",
    [
        ("73654108430135874305", "**4305"),
        ("", "Некорректные данные"),
        ("adcdgfedhssterjjyth", "Некорректные данные"),
        ("1234adcsd", "Некорректные данные"),
    ],
)
def test_get_mask_account(account: Any, mask_account: Any) -> Any:
    """Тестирование маскировки номера счета"""
    assert get_mask_account(account) == mask_account
