#!/usr/bin/env python3
''' last comment here'''
from typing import Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> list:
    '''at last '''
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
