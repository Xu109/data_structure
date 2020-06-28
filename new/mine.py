"""
Author:  Mr.Xu
Create:  2020/6/25 19:20
Github:  https://github.com/WeaponMaster
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""
def merge(nums1, m, nums2, n):
    i = m - 1  # i=2
    j = n - 1  # j=2
    k = m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:  # 把大的数放到nums1的最后一位，倒着放入
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