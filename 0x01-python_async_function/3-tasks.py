#!/usr/bin/env python3
'''using the asyncio library'''
from asyncio import Task, create_task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    '''asyncio task is created'''
    return create_task(wait_random(max_delay))
