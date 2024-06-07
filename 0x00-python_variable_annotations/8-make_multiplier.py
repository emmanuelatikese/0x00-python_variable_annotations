#!/usr/bin/env python3
from typing import Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def mult(a: float) -> float:
        return a * multiplier
    return mult
