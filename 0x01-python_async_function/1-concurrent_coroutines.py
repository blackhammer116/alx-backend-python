#!/usr/bin/env python3
"""
wait random module to run the concurrently
"""

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """
    A function that returns the delay time
    of wait_random 'n' times
    Args:
        n: number of times to execute wait_random
        max_delay: max_delay of the wait
    """
    delay = []
    for i in range(0, n):
        d = wait_random(max_delay)

        delay.append(d)
    return delay
