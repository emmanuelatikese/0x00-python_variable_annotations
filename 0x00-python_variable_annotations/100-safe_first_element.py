#!/usr/bin/env python3
''' this all '''
from typing import Any, Sequence, Union, List


def safe_first_element(lst: Sequence[List[Any]]) -> Union[Any, None]:
    '''ok '''
    if lst:
        return lst[0]
    else:
        return None
