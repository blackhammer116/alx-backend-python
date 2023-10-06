#!/usr/bin/env python3
"""
Optional module for the function argument
"""
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """
    A function that takes a string and [int | float] then returns
    a tuple containing the string and the square of the float
    Args:
        k: string
        v: int OR float
    """
    return (k, pow(v, 2))
