"""
Author:  Mr.Xu
Create:  2020/7/15 13:10
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        if self.next is None:
            return f"{self.data}"
        return f"{self.data}->{self.next}"

def linkMerge(head: Node) -> Node:
    if not head or head.next is None:
        return head
    fast = head
    slow = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    mid = slow.next
    slow.next = None
    return merge(linkMerge(head), linkMerge(mid))


def merge(left: Node, right: Node) -> Node:
    dummy = Node(0)
    cur = dummy
    while left and right:
        if left.data < right.data:
            cur.next = left
            left = left.next
            cur = cur.next
        else:
            cur.next = right
            right = right.next
            cur = cur.next
    if left:
        cur.next = left
    if right:
        cur.next = right
    return dummy.next


if __name__ == '__main__':
    node1 = Node(8)
    node2 = Node(5)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(12)
    node6 = Node(6)
    node7 = Node(2)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    print(node1)
    print(linkMerge(node1))
