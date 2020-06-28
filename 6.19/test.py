"""
Author:  Mr.Xu
Create:  2020/6/20 12:56
Github:  https://github.com/WeaponMaster
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""
from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        cur = self.head
        result = ""
        while cur:
            result += f"{cur}-->"
            cur = cur.next
        return result + "END"

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def insert_head(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def append(self, data):
        if self.head is None:
            self.insert_head(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def insert(self, i, data):
        if self.head is None or i == 1:
            self.insert_head(data)
        else:
            new_node = Node(data)
            cur = self.head
            pre = self.head

            j = 1
            while j < i:
                pre = cur
                cur = cur.next
                j += 1
            pre.next = new_node
            new_node.next = cur

    def delete_head(self):
        if self.head is None:
            print("空链表")
        else:
            self.head = self.head.next

    def pop(self):
        if self.head is None:
            print("空链表")
        else:
            cur = self.head
            while cur.next.next:
                cur = cur.next
            result = cur.next
            cur.next = None
        return result

    def linklist(self, obj: List):
        self.head = Node(obj[0])
        cur = self.head
        for i in obj[1:]:
            cur.next = Node(i)
            cur = cur.next
    def delete_tail(self):
        curr = self.head
        pre = self.head
        while curr.next:
            pre = curr
            curr = curr.next
        result = curr
        pre.next = None
        return result

if __name__ == '__main__':
    l1 = LinkList()
    l1.linklist([1, 2, 3])
    l1.insert_head(100)
    l1.insert_head(99)
    l1.insert_head(98)
    l1.append(3)
    l1.append(2)
    l1.append(1)
    l1.insert(3, 5)
    l1.delete_head()
    print(l1.pop())
    # l1.print_list()
    # print("----------------------------")
    print(l1)
