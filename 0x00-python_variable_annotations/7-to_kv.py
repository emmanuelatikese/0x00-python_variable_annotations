#!/usr/bin/env python3
'''this is all fun'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''fun begin'''
    return (k, v * v)
