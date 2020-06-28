"""
Author:  Mr.Xu
Create:  2020/6/24 15:08
Github:  https://github.com/WeaponMaster
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""
from typing import Optional, Any


class Node:
    def __init__(self, data: Any, next: Optional = None):
        self.data: Any = data
        self.next: Optional = next

    def __repr__(self):
        return f"Node({self.data})"


class LinkedQueue:
    def __init__(self) -> None:
        self.front: Optional[Node] = None
        self.rear: Optional[Node] = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.front is None

    def put(self, item: Any) -> None:
        node: Node = Node(item)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            # assert isinstance(self.rear,Node)
            self.rear.next = node
            self.rear = node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty queue")
        else:
            node: Node = self.front
            self.front = node.next
        self.size -= 1
        return node

    def __repr__(self):
        current = self.front
        result = ""
        while current:
            result += f"{current}<--"
            current = current.next
        return result + "END"

    def get(self, index) -> Any:
        if index < 0 or index >= self.size:
            raise Exception("您的下标已越界")
        else:
            current = self.front
            for i in range(index):
                current = current.next
        return current.data

if __name__ == '__main__':
    q = LinkedQueue()
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    print(q)
    print(q.dequeue())
    print(q)
    print(q.is_empty())
    print(q.get(1))