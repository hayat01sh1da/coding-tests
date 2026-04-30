from __future__ import annotations


def __to_int_with_rescue__(n: str) -> int | str:
    try:
        return int(n)
    except ValueError:
        return 'Not Integer'
