#!/usr/bin/env python3
'''this is all about measuring the time'''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''this is all about measuring'''
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(wait_n(n, max_delay))
    end_time = time.time()
    return ((end_time - start_time) / n)
