"""
Author:  Mr.Xu
Create:  2020/6/23 15:21
Github:  https://github.com/WeaponMaster
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""
from typing import Any, Optional, NoReturn


class Node:
    def __init__(self, data: Any, next: Optional = None) -> NoReturn:
        self.data: Any = data
        self.next: Optional = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkedStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __repr__(self):
        current = self.top
        result = ""
        while current:
            result += f"{current}-->"
            current = current.next
        return result + "END"

    def is_empty(self):
        return self.top is None

    def push(self, data):  # 进栈
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):  # 出栈
        if self.top is None:
            raise IndexError("Pop from empty stack")
        else:
            result = self.top
            self.top = self.top.next
            self.size -= 1
            return result

    def print_linkedstack(self):
        curr = self.top
        while curr:
            print(curr.data, end=" ")
            curr = curr.next

    def capacity(self):
        return self.size

    def peek(self):
        if self.top:
            return self.top.data
        else:
            raise IndexError("Pop from empty stack")


if __name__ == '__main__':
    l = LinkedStack()
    l.push(1)
    l.push(2)
    l.push(3)
    l.push(4)
    print(l)
    print(l.top)
    print(l.pop())
    print(l)
    print(l.peek())
    print(l.is_empty())
    l.print_linkedstack()
