"""
Author:  Mr.Xu
Create:  2020/7/10 14:10
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""
from randomList import randomList
from typing import *

ilist = randomList.randomList(20)

def bubbleSort(l: List[int]):
    if len(l) <= 1:
        return l
    for i in range(1, len(l)):
        flag = False
        for j in range(len(l) - i):
            if l[j] >= l[j + 1]:
                flag = True
                l[j], l[j + 1] = l[j + 1], l[j]
        if not flag:
            break
        print("第{}轮排序结果:".format(i), end=" ")
        print(l)
    return l


if __name__ == '__main__':
    print(ilist)
    print(bubbleSort(ilist))
