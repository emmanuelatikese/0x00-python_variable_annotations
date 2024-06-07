#!/usr/bin/env python3
'''alright'''
from typing import List, Sequence, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''start'''
    return [(i, len(i)) for i in lst]
