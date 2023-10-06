#!/usr/bin/env python3
"""
"""
from typing import Iterable


def element_length(lst: Iterable):
    return [(i, len(i)) for i in lst]
