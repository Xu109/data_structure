"""
Author:  Mr.Xu
Create:  2020/6/19 10:04
Github:  https://github.com/WeaponMaster
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""

class Array():
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    def insert(self, index, element):
        """
        :param index:插入值的位置
        :type index:int
        :param element:插入的值
        :type element:any
        :return:
        :rtype:
        """
        if index < 0 or index > self.size:
            raise Exception('数组越界')
        if self.size >= len(self.array):
            self.addcapacity()
        for i in range(self.size - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def addcapacity(self):
        new_array = [None] * len(self.array) * 2
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def remove(self, index):
        if index < 0 or index > self.size:
            raise Exception('数组越界')
        for i in range(index, self.size):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    def output(self):
        for i in range(self.size):
            print(self.array[i], end='->')


if __name__ == '__main__':
    a = Array(6)
    a.insert(0, 0)
    a.insert(1, 1)
    a.insert(2, 2)
    a.insert(3, 3)
    a.insert(4, 4)
    a.insert(5, 5)
    a.insert(3, 5)
    a.output()
    a.remove(4)
    print('\t')
    a.output()
