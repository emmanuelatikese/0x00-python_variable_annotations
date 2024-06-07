#!/usr/bin/env python3
from typing import Any, Sequence, Union, List


def safe_first_element(lst: Sequence[List[Any]]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
