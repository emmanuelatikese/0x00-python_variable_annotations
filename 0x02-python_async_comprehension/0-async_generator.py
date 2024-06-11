#!/usr/bin/env python3
'''this is a gen func'''
import asyncio
from random import uniform


async def async_generator() -> None:
    '''async function starts here'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
