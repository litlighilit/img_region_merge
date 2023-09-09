"gen a new image from two input images with each taking place one half part"

from __future__ import annotations

# typing
#from typing import Sequence, Iterable
from typing import SupportsInt, Type
from enum import IntEnum
# export
from math import tau as TAU, pi as PI
from collections.abc import Collection, Sequence, Iterable, Callable

Angle = float # XXX: note all of the following three is just the same as float
Rad = Angle # radian
Deg = Angle # degree
class AngleType(IntEnum):
    Rad = 0
    Deg = 1
def high(typ: AngleType) -> Angle: # typ
    if typ is AngleType.Rad: return TAU
    elif typ is AngleType.Deg: return 360
    else: raise ValueError("impossibly reached block") # to comfort typing
Vector2I = tuple[int, int]


def vec2i(x: SupportsInt, y: SupportsInt) -> Vector2I:
    return (int(x), int(y))


Vector2 = tuple[float, float]
