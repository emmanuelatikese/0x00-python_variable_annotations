#!/usr/bin/env python3
'''changing the name of function'''
from typing import List
task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''this is all about concurrent'''
    res = []
    for _ in range(n):
        res.append(await task_wait_random(max_delay))
    return sorted(res)
