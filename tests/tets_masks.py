from src.masks import get_mask_card_number

import pytest


@pytest.mark.parametrize("card_number, mask_card_number", [
    ("1596837868705199", "159683******5199"),
    ("7619804582344591", "761980******4591")
])

def test_get_mask_card_number(card_number: str, mask_card_number: str) -> str:
    assert get_mask_card_number(card_number) == mask_card_number