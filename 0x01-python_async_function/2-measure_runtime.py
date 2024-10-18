#!/usr/bin/env python3.8
'''
File: 2-measure_runtime.py
'''
import asyncio
from time import perf_counter

imported_func = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Calculates average execution time of a group of coroutines
    '''
    start_time = perf_counter()
    asyncio.run(imported_func(n, max_delay))
    end_time = perf_counter()
    return (end_time - start_time)
