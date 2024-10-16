#!/usr/bin/env python3
'''Task 2: Run time for four parallel comprehensions'''
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measures coroutine runtime'''
    routines = []
    for _ in range(4):
        routines.append(async_comprehension())
    start = time.time()
    await asyncio.gather(*routines)
    end = time.time()
    return end - start
