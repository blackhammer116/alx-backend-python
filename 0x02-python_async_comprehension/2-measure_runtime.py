#!/usr/bin/env python3
"""
asyncio for async functions
time to determine the total elapsed time
async_comprehension function that gets tested
"""
import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    A function that returns the total elapsed/run time
    """
    start = time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = time()
    return (end - start)
