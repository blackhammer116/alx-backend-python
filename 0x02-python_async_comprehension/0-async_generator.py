#!/usr/bin/env python3
"""
asyncio for the async function
random for uniform method
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    A function that yields a random float from
    range 0-10 while waiting 1 sec
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
