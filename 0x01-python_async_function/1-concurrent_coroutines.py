#!/usr/bin/env python3
'''multiple concurrent'''
from typing import List
from asyncio import as_completed, create_task
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''this is all about concurrent'''
    res = []
    for _ in range(n):
        res.append(create_task(wait_random(max_delay)))
    return [await x for x in as_completed(res)]
