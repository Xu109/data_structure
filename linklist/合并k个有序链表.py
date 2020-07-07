"""
Author:  Mr.Xu
Create:  2020/7/6 11:53
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""
"""
23 - 合并 k 个排序链表
题目描述
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""
from typing import List
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    def __repr__(self):
        if self.next is None:
            return f"{self.val}"
        return f"{self.val}->{self.next}"

def mergeKLists(lists: List[ListNode]) -> ListNode:
    def merge2Lists(list1, list2):
        """list1和list2分别是两个链表的头结点"""
        dummy = ListNode(0)  # 新建一个虚拟节点
        cur = dummy  # cur用来拆入新节点
        while list1 and list2:  # 两个链表都不为空时
            if list1.val < list2.val:
                cur.next = list1  # 插入新节点
                cur = list1  # cur指向新插入的节点
                list1 = list1.next  # 移动list1
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        return dummy.next

    res = None

    def divideMergeKLists(lists):
        """合并 k 个排序链表"""
        nonlocal res  # 声明外部函数变量
        k = len(lists)
        temp = []
        if k == 0:
            return  # lists为空，直接结束
        if k == 1:  # 归并结束
            res = lists[0]  # 把最后的结果传进res
            return
        for i in range(0, k, 2):
            if i + 1 == k:  # k为奇数，i的最后一个取值是k-1，此时i+1已经超出范围
                temp.append(lists[i])
                break
            # 如果k为偶数，i的最后一个取值永远是k-2
            temp.append(merge2Lists(lists[i], lists[i + 1]))
        divideMergeKLists(temp)

    divideMergeKLists(lists)
    return res

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(4)
    node3 = ListNode(5)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(1)
    node5 = ListNode(3)
    node6 = ListNode(4)
    node4.next = node5
    node5.next = node6

    node7 = ListNode(2)
    node8 = ListNode(6)
    node7.next = node8

    list0 = [node1, node4, node7]
    print(mergeKLists(list0))