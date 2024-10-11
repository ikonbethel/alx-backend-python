#!/usr/bin/env python3
'''Module containing safely_get_value'''
from typing import TypeVar, Union, Mapping, Any


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    '''Safely get a value from a dictionary'''
    if key in dct:
        return dct[key]
    else:
        return default
