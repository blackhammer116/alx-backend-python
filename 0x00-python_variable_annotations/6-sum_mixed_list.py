#!/usr/bin/env python3
"""
Union module to annotate a mixed list
"""
from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """
    A function that takes a mixed list and returns their sum
    as float
    Args:
        mxd_lst: list of int and float
    """
    return sum(mxd_lst)
