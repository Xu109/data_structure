"""
Author:  Mr.Xu
Create:  2020/6/24 14:24
Github:  https://github.com/WeaponMaster
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""
# from queue import Queue


class Queue:
    def __init__(self):
        self.entries = []
        self.length = 0

    def __str__(self):
        printed = "<" + str(self.entries)[1:-1] + ">"
        return printed

    def put(self, item):
        self.entries.append(item)
        self.length += 1

    def get(self):
        dequeued = self.entries[0]
        self.length = self.length - 1
        self.entries = self.entries[1:]
        return dequeued

    def front(self):
        return self.entries[0]

    def rotate(self, rotation):
        for i in range(rotation):
            self.put(self.get())

    def capacity(self):
        return self.length


q = Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
print(q)
print(q.get())
print(q)
