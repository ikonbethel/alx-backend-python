#!/usr/bin/env python3
'''Task 4: Tasks'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Takes in 2 int arguments (in this order): n and max_delay.
    You will spawn wait_random n times with the specified max_delay.
    wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order
    without using sort() because of concurrency
    '''
    result: List[float] = []
    inserted = False
    for _ in range(n):
        delayed_value = await task_wait_random(max_delay)
        for i in range(len(result)):
            inserted = False
            if delayed_value < result[i]:
                result.insert(i, delayed_value)
                inserted = True
                break
        if not inserted:
            result.append(delayed_value)
    return result
