#!/usr/bin/env python3
''' this is all about '''
from typing import Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''about fini'''
    def mult(a: float) -> float:
        return a * multiplier
    return mult
