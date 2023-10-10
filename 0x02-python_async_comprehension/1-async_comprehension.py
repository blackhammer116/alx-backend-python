#!/usr/bin/env python3
"""
asyncio for async functions
List for type-annotations
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A function that returns the ten random numbers
    generated from the async_generator function
    """
    return [i async for i in async_generator()]
