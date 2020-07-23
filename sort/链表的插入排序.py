"""
Author:  Mr.Xu
Create:  2020/7/14 12:34
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

def linkInsert(head: Node):
    if head is None or head.next is None:
        return head
    dummy = Node(0)
    curr = head
    pre = dummy
    while curr:
        temp = curr.next
        while pre.next is not None and pre.next.data < curr.data:
            pre = pre.next
        curr.next = pre.next
        pre.next = curr
        curr = temp
        pre = dummy
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
    print(linkInsert(node1))

