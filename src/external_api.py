from typing import Any

import requests
import os
from dotenv import load_dotenv


load_dotenv()
values = os.getenv("PASSWORD")
# keys = os.getenv("API_KEY")
# headers = {keys: values}


def conversion(trans1: Any) -> Any:
    """Функция конвертации"""
    amout = trans1["operationAmount"]["amount"]
    code = trans1["operationAmount"]["currency"]["code"]
    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={code}&amount={amout}"
    payload = {}
    response = requests.get(url, headers={"apikey": values}, data=payload)
    result = response.json()
    return result["result"]