"""
Author:  Mr.Xu
Create:  2020/6/29 9:39
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""


def hamingDistance(x: int, y: int) -> int:
    a = x ^ y
    count = 0
    while a != 0:
        a = a & (a - 1)
        count += 1
    return count
