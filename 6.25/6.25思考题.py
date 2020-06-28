"""
Author:  Mr.Xu
Create:  2020/6/29 1:17
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""
'''分离指针专题
分离指针是指两个指针分别在两个容器中移动；
根据问题的不同，初始位置可能都在头部，或者都在尾部，或一头一尾

349 - 两个数组的交集
题目描述
给定两个数组，编写一个函数来计算它们的交集。

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [9,4]

说明:
输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。'''




from typing import List
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()
    i = 0
    j = 0
    num_set = set()
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            num_set.add(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return list(num_set)


'''————————————————
版权声明：本文为CSDN博主「愉悦的麻婆豆腐」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/u010788049/java/article/details/81437834

88 - 合并两个有序数组
https://leetcode-cn.com/problems/merge-sorted-array/
题目描述
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
'''


def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while i >= 0:
        nums1[k] = nums1[i]
        k -= 1
        i -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1
    return nums1

# 二分查找


def binarySearch(nums: List, val: int):
    left = 0
    right = len(nums) - 1
    while left <= right:
        if val not in nums:
            return -1
        if val == nums[left]:
            return left
        elif val == nums[right]:
            return right
        else:
            mid = (left + right) // 2
            if val < nums[mid]:
                right = mid
            elif val > nums[mid]:
                left = mid
            else:
                return mid


def binarySearch2(nums: List, val: int):
    left = -1
    right = len(nums)
    while left <= right:
        if val not in nums:
            return -1
        mid = (left + right) // 2
        if val < nums[mid]:
            right = mid
        elif val > nums[mid]:
            left = mid
        else:
            return mid


def binarySearch3(nums: List, val: int):
    left = -1
    right = len(nums)
    while left <= right:
        mid = left + (right - left) // 2
        if val < nums[mid]:
            right = mid
        elif val > nums[mid]:
            left = mid
        else:
            return mid


def binarySearch4(nums: List, val: int, left: int, right: int):
    if right > 0:
        mid = left + (right - left) // 2
        if nums[mid] == val:
            return mid
        elif nums[mid] > val:
            return binarySearch4(nums, val, left, mid - 1)
        else:
            return binarySearch4(nums, val, mid + 1, right)
    else:
        return -1


if __name__ == '__main__':
    a = list(range(20))
    print(binarySearch4(a, 9, 0, 19))
