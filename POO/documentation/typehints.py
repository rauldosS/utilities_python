"""
    documentation for this module

    Typing - https://docs.python.org/3/library/typing.html
"""

from typing import Union

x: int =    10
y: float =  10.5
z: bool =   False

def function(p1: float, p2: str, p3:dict) -> float:
    return p1, p2, p3

def function(p1: float) -> Union[list, dict]:
    return []