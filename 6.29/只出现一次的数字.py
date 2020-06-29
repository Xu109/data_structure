"""
Author:  Mr.Xu
Create:  2020/6/29 10:10
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""
from typing import List
def singleNumber(nums: List[int]):
    res = 0
    for i in nums:
        res = res ^ i
    return res


if __name__ == '__main__':
    a = [2,1,3,1,3]
    print(singleNumber(a))