"""
Author:  Mr.Xu
Create:  2020/6/29 10:19
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""

from typing import List


def hamingDistanceSum(nums: List) -> int:
    count = 0
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            a = nums[i] ^ nums[j]
            while a != 0:
                a = a & (a - 1)
                count += 1
    return count


def hamingDistanceSum2(nums: List) -> int:
    res = 0
    for i in range(32):
        count_0 = 0
        count_1 = 0
        for j in range(len(nums)):
            if (nums[j] >> i) & 1:
                count_1 += 1
            else:
                count_0 += 1
        res += count_0 * count_1
    return res


a = [4, 14, 2]
print(hamingDistanceSum2(a))
