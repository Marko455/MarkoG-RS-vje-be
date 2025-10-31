import re

def validiraj_broj_telefona(broj: str) -> str | None:
    if not broj:
        return None

    ociscen = re.sub(r"[^\d+]", "", broj)

    if ociscen.count('+') > 1:
        return None

    if '+' in ociscen and not ociscen.startswith('+'):
        return None

    return ociscen