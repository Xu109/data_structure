"""
Author:  Mr.Xu
Create:  2020/7/6 11:39
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""
'''
61 - 旋转链表
题目描述
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"{self.data}->{self.next}"

def rotateRight(head: Node, k):
    if head is None:
        return None
    n = 1
    curr = head
    while curr.next:
        curr = curr.next
        n += 1
    curr.next = head
    end = head
    for i in range(n - (k % n) - 1):
        end = end.next
    new_head = end.next
    end.next = None
    return new_head


def rotateRight1(head: Node, k):
    if head is None:
        raise Exception("空链表转个啥劲")
    if head.next is None:
        return head
    count = 0
    cur0 = head
    while cur0:
        count += 1
        cur0 = cur0.next
    k = k % count
    for i in range(k):
        cur = head
        pre = head
        while cur.next:
            pre = cur
            cur = cur.next
            if cur.next is None:
                break
        pre.next = None
        cur.next = head
        head = cur
    return head

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print(rotateRight(node1, 2))
    node6 = Node(0)
    node7 = Node(1)
    node8 = Node(2)
    node6.next = node7
    node7.next = node8
    print(rotateRight(node6, 4))