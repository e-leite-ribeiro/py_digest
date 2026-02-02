import os
from dotenv import load_dotenv

load_dotenv()

EXCHANGE_API_URL = os.getenv("EXCHANGE_API_URL")
EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY")

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int (os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")