from config import *
from exchange.client import ExchangeRateClient
from digest.service import DigestService
from digest.sender import EmailSender
import argparse
from decimal import Decimal

def parse_args():
    parser = argparse.ArgumentParser(
        description="Send currency conversion digest by email"
    )

    parser.add_argument(
        "amount",
        type=Decimal,
        help="Amount of money to convert"
    )
    parser.add_argument(
        "base_currency",
        type=str,
        help="Base currency (e.g. USD)"
    )
    parser.add_argument(
        "targets",
        type=str,
        help="Comma-separated target currencies (e.g. EUR,BRL,RUS)"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    amount = args.amount
    base = args.base_currency.upper()
    targets = [c.strip().upper() for c in args.targets.split(",")]

    exchange_client = ExchangeRateClient(base_url=EXCHANGE_API_URL, api_key=EXCHANGE_API_KEY)
    digest_service = DigestService(exchange_client)

    email_sender = EmailSender(
        SMTP_HOST,
        SMTP_PORT,
        SMTP_USER,
        SMTP_PASSWORD
    )
    
    digest = digest_service.build_digest(
        amount=amount,
        base_currency=base,
        targets=targets
    )

    print (digest)
    # email_sender.send(
    #     subject="Currency ratio digest",
    #     body=digest,
    #     sender=EMAIL_FROM,
    #     recipient=EMAIL_TO
    # )

if __name__ == "__main__":
    main()

