import logging
import math
import os
from typing import List

import currencyapicom
from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
load_dotenv(find_dotenv('.env'))
client = currencyapicom.Client(os.getenv("API_KEY"))
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class ConversionRequest(BaseModel):
    input_currency: str
    output_currencies: List[str]
    amount: float
    date: str


class ConversionResponse(BaseModel):
    currency: str
    amount: float | None


@app.post("/api/convert", response_model=List[ConversionResponse])
async def convert_currency(request: ConversionRequest):
    exchange_rates = get_historical_exchange_rates(request)
    results = []

    for output_currency in request.output_currencies:
        rate = exchange_rates.get(output_currency, 0)
        if rate == 0:
            results.append(ConversionResponse(currency=output_currency, amount=None))
        else:
            converted_amount = math.ceil(request.amount * rate * 100) / 100
            results.append(ConversionResponse(currency=output_currency, amount=converted_amount))

    return results


def get_historical_exchange_rates(request: ConversionRequest):
    try:
        response = client.historical(
            request.date,
            request.input_currency,
            request.output_currencies
        )
        logger.debug(f"Exchange rates: {response}")

        exchange_rates = {currency: data['value'] for currency, data in response['data'].items()}
        return exchange_rates
    except Exception as e:
        logger.error(f"Error retrieving exchange rates: {e}")
        raise HTTPException(status_code=500, detail=str(e))
