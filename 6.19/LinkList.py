"""
Author:  Mr.Xu
Create:  2020/6/19 16:17
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
        self.tail = None
        self.size = 0

    def __repr__(self):
        current = self.head
        string_repr = ""
        while current:
            string_repr += f"{current}-->"
            current = current.next
        return string_repr + "END"

    def get(self, index):
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr

    def insert(self, index, data):
        new_node = Node(data)
        if index < 0 or index > self.size:
            raise Exception("数组越界")
        elif self.size == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index == self.size - 1:
            self.tail.next = new_node
            self.tail = new_node
        else:
            prev = self.get(index - 1)
            new_node.next = prev.next
            prev.next = new_node
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise Exception("数组越界")
        elif index == 0:
            remove_node = self.head
            self.head = self.head.next
        elif index == self.size - 1:
            prev = self.get(index - 1)
            remove_node = prev.next
            prev.next = None
            self.tail = prev
        else:
            prev = self.get(index - 1)
            remove_node = prev.next
            prev.next = prev.next.next
        self.size -= 1

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def linklist(self, obj: List):
        new_node = Node(obj[0])
        self.head = new_node
        curr = self.head
        for i in obj[1:]:
            curr.next = Node(i)
            curr = curr.next

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev


if __name__ == '__main__':
    l1 = LinkList()
    l1.insert(0, 1)
    l1.insert(1, 2)
    l1.insert(2, 3)
    l1.insert(3, 4)
    print(l1.get(2))
    print(l1)
    l1.reverse()
    print(l1)
