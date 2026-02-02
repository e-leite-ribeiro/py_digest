from decimal import Decimal
from typing import Dict
from exchange.client import ExchangeRateClient
from digest.formatter import format_digest

class DigestService:
    def __init__(self, exchange_client: ExchangeRateClient):
        self.exchange_client = exchange_client

    def convert_rates(self, amount: Decimal, base_currency: str, rates: Dict[str, Decimal]) -> Dict[str, Decimal]:
        conversion_rate = rates.pop(base_currency)
        values = {}
        for key,value in rates.items():
            values[key] = (value * amount) / conversion_rate
        return values
    
    def build_digest(self, amount: Decimal, base_currency: str, targets: list[str]) -> str:
        symbols = targets + [base_currency]
        rates = {}

        if "BTC" in symbols:
            symbols.remove("BTC")
            rates.update(self.exchange_client.get_btc_rates())

        rates.update(self.exchange_client.get_fx_rates(symbols))
        
        values = self.convert_rates(amount, base_currency, rates)
        return format_digest(amount, base_currency, values)



    