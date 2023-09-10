from __future__ import annotations

from math import atan2
from dataclasses import dataclass
from operator import sub
from typing import TypeVar

from . import Vector2I, AngleType, Rad, Deg, high, Callable, Type, PI, TAU

Point = Vector2I


@dataclass
class RegionInfo:
    x: float
    y: float

    @staticmethod
    def rel(p: Point, origin: Point) -> RegionInfo:
        return RegionInfo(*map(sub, p, origin))

    @property
    def rad(self) -> Rad:
        #    return PI * (1-0.5*self.y_sign)
        rad = atan2(self.y, self.x)
        # if self.y < 0: rad += PI
        return norm_angle(rad, AngleType.Rad)
    @property
    def deg(self) -> Deg:
        return rad2deg(self.rad)

A = TypeVar('A', Deg, Rad)
def region_div(n: int, AngleNotation: AngleType) -> Callable[[A], int]:
    angle_per_reg = high(AngleNotation) / n

    def cal_region_by_angle(r: A) -> int:
        return int(r / angle_per_reg)

    return cal_region_by_angle


def distr_region(n: int, origin: Point, rotate: Deg) -> Callable[[Point], int]:
    # for `rotate`'s doc, see __main__.py
    reg_div = region_div(n, AngleType.Deg)

    def cal_region(p: Point) -> int:
        ang = RegionInfo.rel(p, origin).deg - rotate
        ang = -ang # origin of img is in left-top
        ang = norm_angle(ang, AngleType.Deg)
        res = reg_div(ang)
        return res

    return cal_region

def norm_angle(ang: A, AngleNotation: AngleType) -> A:
    max_ang = high(AngleNotation)
    return ang - max_ang * (ang // max_ang)
def rad2deg(rad: Rad) -> Deg:
    return 180 * rad / PI
def deg2rad(deg: Deg) -> Rad:
    return PI * deg / 180

if __name__ == "__main__":
    reg = RegionInfo.rel(
        (1, 1),
        (1, 2))
    ang = reg.rad
    print(reg.x, reg.y)
    print(ang)
    print(rad2deg(ang))
