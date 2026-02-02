import requests

class ExchangeRateClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key 
    
    def get_rates(self, targets: list[str]) -> dict:
        response = requests.get(
            self.base_url + "?app_id=" + self.api_key,
            params={
                "symbols": ",".join(targets)
            },
            timeout = 10
        )
        response.raise_for_status()
        data = response.json()
        return data["rates"]
