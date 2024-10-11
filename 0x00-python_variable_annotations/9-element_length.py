#!/usr/bin/env python3
'''Module containing element_length'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Returns tuple of Element length'''
    return [(i, len(i)) for i in lst]
