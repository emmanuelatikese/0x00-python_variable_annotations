#!/usr/bin/env python3
'''comprehension function'''
async_generator = __import__('0-async_generator').async_generator
from typing import List


async def async_comprehension() -> List[float]:
    '''comprehension begins'''
    return [x async for x in async_generator()]
