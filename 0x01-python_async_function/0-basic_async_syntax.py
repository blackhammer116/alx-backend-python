#!/usr/bin/env python3
"""
random: module to randomize the wait
time: module to make it sleep
"""
import random
import asyncio

async def wait_random(max_delay = 10.0):
    """
    An async function that waits for a random delay
    and returns it
    """ 
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
