import hashlib


def get_hash(row: str) -> bytes:
    return hashlib.sha256(row.encode("utf-8")).digest()
