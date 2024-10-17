#!/usr/bin/env python3
'''Task 2: Measure run time'''
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    return (end_time - start_time) / n
