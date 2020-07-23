"""
Author:  Mr.Xu
Create:  2020/7/12 20:36
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""

from randomList import randomList
from typing import List

l = randomList.randomList(10)

def bubbleSort(list: List[int]):
    if len(list) <= 1:
        return 1
    for i in range(1, len(list)):
        flag = False
        for j in range(len(list) - i):
            if list[j] >= list[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                flag = True
        if not flag:
            break
        print("第{}轮排序结果:".format(i), end=" ")
        print(list)
    return list

def selectionSort(list: List[int]):
    if len(list) <= 1:
        return 1
    for i in range(len(list) - 1):
        minindex = i
        for j in range(i + 1, len(list)):
            if list[j] < list[minindex]:
                minindex = j
        list[i], list[minindex] = list[minindex], list[i]
        print("第{}轮排序结果:".format(i + 1), end=" ")
        print(list)
    return list

if __name__ == '__main__':
    # bubbleSort(l)
    print(l)
    selectionSort(l)