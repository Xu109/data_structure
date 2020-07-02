"""
Author:  Mr.Xu
Create:  2020/7/2 16:20
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""
"""
leetcode 21
题目描述
将两个有序链表合并为一个新的有序链表并返回。
新链表是通过拼接给定的两个链表的所有节点组成的。

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
思路
这里我们可以用到归并排序的思维。

我们维护一个 cur 指针，我们需要做的是调整它的 next 指针。
如果 l1 当前位置的值小于等于 l2 ，我们就把 l1 的值接在 cur 节点的后面
同时将 l1 指针往后移一个。否则，我们对 l2 做同样的操作。
不管我们将哪一个元素接在了后面，我们都把 cur 向后移一个元素。

在循环终止的时候， l1 和 l2 至多有一个是非空的。
由于输入的两个链表都是有序的，所以不管哪个链表是非空的，
它包含的所有元素都比前面已经合并链表中的所有元素都要大。
这意味着我们只需要简单地将非空链表接在合并链表的后面，并返回合并链表。
"""

from typing import Optional
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"
def mergeTwoLists(head1: Optional[Node],head2: Optional[Node]):
    if head1 is None or head2 is None:
        raise Exception("传入的链表存在空链表")
    dummy = Node(0)
    cur = dummy
    curr1 = head1
    curr2 = head2
    while curr1 and curr2:
        if curr1.data <= curr2.data:
            cur.next = curr1
            curr1 = curr1.next
        else:
            cur.next = curr2
            curr2 = curr2.next
        cur = cur.next
    if curr1:
        cur.next = curr1
    if curr2:
        cur.next = curr2
    return dummy.next


