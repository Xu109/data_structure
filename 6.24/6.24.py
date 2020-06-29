"""
Author:  Mr.Xu
Create:  2020/6/24 11:21
Github:  https://github.com/WeaponMaster
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""

# 三数之和
from typing import List


def threeSum(nums: List[int]) -> List:
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] > 0:
                right -= 1
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            else:
                res.append(nums[i], nums[left], nums[right])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return res
# 最接近的三数之和

def threeSumClossest(nums: List[int], target: int) -> int:
    nums.sort()
    min = abs(nums[0] + nums[1] + nums[2] - target)
    res = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sums = nums[i] + nums[left] + nums[right]
            if abs(sums - target) < min:
                min = abs(sums - target)
                res = sums
            if sums > target:
                right -= 1
            elif sums < target:
                left += 1
            else:
                return sums
    return res
