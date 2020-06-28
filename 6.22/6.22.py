"""
Author:  Mr.Xu
Create:  2020/6/22 15:45
Github:  https://github.com/WeaponMaster
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""
'''题目1
leetcode 27 移除元素
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O (1) 额外空间的条件下完成。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
示例 1:

给定 nums = [3,2,2,3], val = 3, 函数应该返回新的长度 2,
并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。

示例 2:

给定 nums = [0,1,2,2,3,0,4,2], val = 2, 函数应该返回新的长度 5,
并且 nums 中的前五个元素为 0, 1, 3, 0, 4。注意这五个元素可为任意顺序。
你不需要考虑数组中超出新长度后面的元素。'''




from typing import List
def removeELement(nums: List[int], val: int) -> int:
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
        else:
            fast += 1
    return slow


l2 = [0, 1, 2, 2, 3, 0, 4, 2]
print(removeELement(l2, 2))
print(l2)

'''题目2
leetcode 283 - 移动零
问题描述
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。


思路
i 指针用于存放非零元素
j 指针用于遍历寻找非零元素
（注：j 指针找到一个非零元素后，nums[i] 的位置 i++，用于下一个 j 指针找到的非零元素）
j 指针遍历完后，最后 nums 数组还有空位置，存放 0 即可'''


def removeZero(nums: List[int]) -> int:
    i = 0
    j = 0
    while j < len(nums):
        if nums[j] != 0:
            nums[i] = nums[j]
            i += 1
            j += 1
        else:
            j += 1
    for k in range(i, len(nums)):
        nums[k] = 0


l1 = [0, 1, 0, 3, 12]
removeZero(l1)
print(l1)

'''题目3
LeetCode 80 - 删除排序数组中的重复项
题目描述
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O (1) 额外空间的条件下完成。

示例 1:

给定 nums = [1,1,1,2,2,3], 函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
你不需要考虑数组中超出新长度后面的元素。

示例 2:

给定 nums = [0,0,1,1,1,1,2,3,3], 函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。
你不需要考虑数组中超出新长度后面的元素。

思路
遍历整个表：

把当前的元素与它前面的对比，如果二者元素相同（为重复元素）：
此时统计重复的计数器 count+=1。题目要求只保留 2 个重复的元素，这里需要加入重复元素个数的判断：

这个元素正好重复了 2 次 => 则进行保留。列表长度 i+=1，然后 nums[i]=nums[j]；
这个元素重复多于 2 次 => 不进行任何操作。体现在程序上不做处理
把当前的元素与它前面的对比，如果二者元素不同（为新元素）：此时把当前这个结点 (nums[j]) 添加到新表里面去，nums[i] = nums[j], 表长 i+1'''
def remove2(nums: List[int]) -> int:
    count = 1
    slow = 0
    fast = 1
    # [1,1,1,2,2,3,4]
    while fast < len(nums):
        if nums[slow] == nums[fast]:
            count += 1
            if count == 2:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        else:
            slow += 1
            nums[slow] = nums[fast]
            count = 1
            fast += 1
    return slow + 1

'''题目4:
判断链表有没有环
'''


def is_circle(head):
    curr = head
    prev = head
    while curr and prev.next:
        curr = curr.next.next
        if prev == curr:
            return True
        prev = prev.next
    return False

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None
print(is_circle(node1))
