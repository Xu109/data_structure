"""
Author:  Mr.Xu
Create:  2020/7/9 12:46
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""
'''
42 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

'''
# 暴力解法
from typing import List
def trap1(height: List[int])-> int:
    res = 0
    size = len(height)
    for i in range(size):
        leftmax = 0
        rightmax = 0
        for j in range(i, size):
            rightmax = max(height[j], rightmax)
        for j in range(i, -1, -1):
            leftmax = max(height[j], leftmax)
        res = res + min(leftmax, rightmax) - height[i]
    return res

def trap2(height: List[int])-> int:
    n = len(height)
    if n == 0 or n == 1 or n == 2:
        return 0
    left = 0
    right = n - 1
    res = 0
    l_max = height[0]
    r_max = height[n - 1]
    while left <= right:
        l_max = max(l_max, height[left])
        r_max = max(r_max, height[right])
        if l_max < r_max:
            res += l_max - height[left]
            left += 1
        elif l_max >= r_max:
            res += r_max - height[right]
            right -= 1
    return res

def trap(list):
    # 记录指针移动过程中的高峰
    movepeak = 0
    # 记录面积
    area = 0
    # 记录整体最高柱子的index
    maxindex = 0
    # 先遍历数组找到最大那块板的index
    for i in range(1, len(list)):
        if list[i] > list[maxindex]:
            maxindex = i
    for i in range(0, maxindex):
        if movepeak < list[i]:
            # 遇到新的高峰，就更新移动最高峰
            movepeak = list[i]
        else:
            # 面积的宽度始终为1,面积计算只需加上高度即可
            area += movepeak - list[i]
    # 重置高峰
    movepeak = 0
    # 从右向左遍历
    for j in range(len(list) - 1, maxindex, -1):
        if movepeak < list[j]:
            movepeak = list[j]
        else:
            area += movepeak - list[j]
    return area


if __name__ == '__main__':
    a = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap2(a))
