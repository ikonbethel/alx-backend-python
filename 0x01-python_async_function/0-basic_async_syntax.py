#!/usr/bin/env python3
'''Task 0: Basics of Async'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    Takes in an integer argument:
    (max_delay,with a default value of 10)
    and waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it.
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return (delay)
