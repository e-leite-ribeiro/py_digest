# py_digest

A simple currency converter written in python3 that converts an amount in a base currency to specified target currencies and sends an email digest to the user

## Getting Started

This project requires:

- `python-dotenv` for loading `.env` variables
- `requests` for fetching data from the exchange API of your preference

Requirements can be installed with pip:

```bash
> pip install -r requirements.txt
```

I used the free api service from "https://openexchangerates.org/api/latest.json" and a smtp service for notification. Check the .env.example file to see the necessary tokens and authentications you will need to run the app please.

## Running

Inside the project directory run:

```bash
> python3 app.py <amount> <base_currency_code> <target_currencies_list>
```

Parameters

- `<amount>` - should be a decimal in the format xyz.ab
- `<base_currency_code>` - case insensitive code for a currency (e.g USD, brl, etc..)
- `<target_currency_code>` - case insensitive codes for currencies separated by commas (e.g RUB,EUR,BRL)

## Use case

example of input and output:

```bash
> python3 app.py 1000.5 brl eur,USD,Rub
```

should generate an email body in this fashion:

```text
Currency Digest -- 2026-02-02T18:43:19.679530+00:00 UTC

1000.5 BRL is worth:

161.27 EUR
14548.33 RUB
190.30 USD
```
