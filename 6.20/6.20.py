"""
Author:  Mr.Xu
Create:  2020/6/21 13:40
Github:  https://github.com/WeaponMaster
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""

"""
leetcode第026题数组去重(删除排序数组中的重复项)

给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
"""

# 方案一




from typing import List
class Solution:
    def removeDuplicated(self, nums: List[int]) -> int:
        n = len(set(nums))
        i = 0
        while i < n - 1:
            if nums[i] == nums[i + 1]:
                temp = nums[i + 1]
                nums[i + 1:len(nums) - 1] = nums[i + 2:]
                nums[-1] = temp
                continue
            else:
                i += 1
        return i + 1

# 方案二
# TODO
    def removeDuplicated(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return slow + 1


'''
今天思考题:leetcode27
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O (1) 额外空间的条件下完成。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
示例 1:
给定 nums = [3,2,2,3], val = 3, 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。
示例 2:
给定 nums = [0,1,2,2,3,0,4,2], val = 2, 函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。'''


def removeval(nums: List[int], val) -> int:
    n = len(nums) - nums.count(val)
    i = 0
    while i < n:
        if nums[i] == val:
            nums[i:len(nums) - 1] = nums[i + 1:]
            nums[-1] = val
            continue
        else:
            i += 1
    return i


a = Solution()
b = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(a.removeDuplicated(b))
print(b)
nums = [0, 1, 2, 2, 3, 0, 4, 2]
print(removeval(nums, 2))
print(nums)
