"""
Author:  Mr.Xu
Create:  2020/7/14 11:34
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""
from randomList import randomList
from typing import *
ilist = randomList.randomList(20)


def insertSort(l: List) -> List:
    if len(l) <= 1:
        return l
    for right in range(1, len(l)):
        target = l[right]
        for left in range(0, right):
            if l[left] > target:
                l[left + 1:right + 1] = l[left: right]
                l[left] = target
                break
        print("第{}轮排序结果:".format(right), end=" ")
        print(l)
    return l


if __name__ == '__main__':
    insertSort(ilist)
    print("最终的排序结果为:", ilist)
