from decimal import Decimal
import requests

GRAMS_PER_TROY_OUNCE = Decimal("31.1034768")

class ExchangeRateClient:
    def __init__(self, fx_base_url: str, fx_api_key: str, btc_base_url: str):
        self.fx_base_url = fx_base_url
        self.fx_api_key = fx_api_key
        self.btc_base_url = btc_base_url
    
    def get_fx_rates(self, targets: list[str]) -> dict:
        response = requests.get(
            self.fx_base_url + "?app_id=" + self.fx_api_key,
            params={
                "symbols": ",".join(targets)
            },
            timeout = 10
        )
        response.raise_for_status()
        data = response.json()
        rates = {currency: Decimal(str(rate)) for currency, rate in data["rates"].items()}
        if rates["XAU"] :
            rates["XAU"] = rates["XAU"] * GRAMS_PER_TROY_OUNCE
        return rates

    def get_btc_rates(self) -> dict:
        response = requests.get(
            self.btc_base_url,
            timeout = 10
        )
        response.raise_for_status()
        data = response.json()
        btc_per_usd = Decimal("1") / Decimal(str(data["USD"]["last"]))
        return {"BTC": btc_per_usd}
