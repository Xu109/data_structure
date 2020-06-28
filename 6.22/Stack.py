"""
Author:  Mr.Xu
Create:  2020/6/23 14:38
Github:  https://github.com/WeaponMaster
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""


class Stack:
    def __init__(self, limit=10):
        self.stack = []
        self.size = 0

    def __bool__(self):
        return bool(self.stack)

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        if len(self.stack) < self.size:
            raise Exception('stackoverflow')
        self.stack.append(data)
        self.size += 1

    def pop(self):
        if self.stack:
            temp = self.stack.pop()
            self.size -= 1
            return temp
        else:
            raise Exception('pop from an empty stack')

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        return self.size

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    stack.push(4)
    print(stack)
    print(stack.peek())
    print(bool(stack))
    print(stack.is_empty())