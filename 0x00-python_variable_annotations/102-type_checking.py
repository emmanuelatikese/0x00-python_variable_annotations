#!/usr/bin/python3
from typing import Tuple, List, Any


def zoom_array(lst: List[int], factor: int = 2) -> List[Tuple[Any]]:
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)