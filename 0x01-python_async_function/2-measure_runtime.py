#!/usr/bin/env python3
"""
time for getting the total elapsed time
wait_n function that gets tested
asyncio for async functions
"""
import importlib
from time import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    A function that returns total elaplsed time
    divided by n
    Args:
        n: number of executions for wait_n
        max_delay: the maximum delay time
    """
    start = time()
    asyncio.run(wait_n(n, max_delay))
    end = time()

    result = (end - start) / n

    return result
