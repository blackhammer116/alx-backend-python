#!/usr/bin/env python3
"""
asyncio for async functions
wait_random imported from the first task
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    A function that returns an asyncio task 
    """
    return asyncio.ensure_future(wait_random(max_delay))
