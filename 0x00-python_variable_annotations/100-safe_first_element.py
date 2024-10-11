#!/usr/bin/env python3
'''Module containing safe_first_element'''
from typing import Sequence, Any, Union


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Safely retrieve first element in a list'''
    if lst:
        return lst[0]
    else:
        return None
