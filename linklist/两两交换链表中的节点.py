"""
Author:  Mr.Xu
Create:  2020/7/6 11:39
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""
'''
24 - 两两交换链表中的节点
题目描述
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
给定 1->2->3->4, 你应该返回 2->1->4->3.
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self.next is None:
            return f"{self.val}"
        return f"{self.val}->{self.next}"


def swapPairs1(head: ListNode) -> ListNode:
    if not head:
        return head
    dummy = ListNode(0)
    dummy.next = head
    cur = dummy
    while head and head.next:
        node1 = head
        node2 = head.next
        cur.next = node2
        node1.next = node2.next
        node2.next = node1
        cur = node1
        head = node1.next
    return dummy.next


def swapPairs(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    pre = dummy
    while pre.next and pre.next.next:
        slow = pre.next
        fast = pre.next.next
        pre.next = fast
        slow.next = fast.next
        fast.next = slow
        pre = pre.next.next
    return dummy.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    print(node1)
    print(swapPairs(node1))
