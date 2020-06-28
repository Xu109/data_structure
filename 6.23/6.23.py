"""
Author:  Mr.Xu
Create:  2020/6/23 11:58
Github:  https://github.com/WeaponMaster
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""

# 两数之和
from typing import List


def two_sum(nums: List[int], target: int):
    result = []
    for i in range(len(nums)):
        for j in nums[i + 1:]:
            if nums[i] + j == target:
                result.append(nums[i])
                result.append(j)
    return result


def twoSum(nums, target):
    nums_dict = {}
    for i in range(len(nums)):
        temp = target - nums[i]
        if temp in nums_dict:
            return [nums_dict[temp], i]
        else:
            nums_dict[nums[i]] = i


def twosum(nums, target):
    begin = 0
    end = len(nums) - 1
    while begin < end:
        curr = nums[begin] + nums[end]
        if curr == target:
            print(begin, end)
            begin += 1
            end -= 1
            break
        else:
            if curr < target:
                begin += 1
            else:
                end -= 1

