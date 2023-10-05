#!/usr/bin/env python3
"""
Necessary modules for variable annotations
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    function to return the length of an element
    """
    return [(i, len(i)) for i in lst]
