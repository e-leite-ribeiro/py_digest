from datetime import datetime, timezone
from decimal import Decimal

def format_digest(amount: Decimal, base: str, rates: dict) -> str:
    lines = [
        f"Currency Digest -- {datetime.now(timezone.utc).isoformat()} UTC",
        "",
        f"{amount} {base} is worth:",
        ""
    ]

    for currency, value in rates.items():
        lines.append(f"{value:.2f} {currency}")
    return "\n".join(lines)