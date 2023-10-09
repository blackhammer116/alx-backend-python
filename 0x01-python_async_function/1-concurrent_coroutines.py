#!/usr/bin/env python3
"""
importlib for sorting out the list
asyncio for async functions
list module for annotation
wait random module to run the concurrently
"""
import importlib
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    A function that returns the delay time
    of wait_random 'n' times
    Args:
        n: number of times to execute wait_random
        max_delay: max_delay of the wait
    """
    tasks = []
    delays = []
    for i in range(n):
        task = asyncio.ensure_future(wait_random(max_delay))
        tasks.append(task)

    for task in tasks:
        delay = await task
        delays.append(delay)

    delays = sorted(delays)

    return delays
