#!/usr/bin/env python3
"""
Callable module used to return another Callable function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A function that returns another Callable function
    Args:
        multiplier: float
    """
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
