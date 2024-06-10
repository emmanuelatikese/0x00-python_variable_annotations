#!/usr/bin/env python3
'''this is all about waiting'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''this where everything start'''
    new_time = random.uniform(0, max_delay)
    await asyncio.sleep(new_time)
    return new_time
