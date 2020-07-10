"""
Author:  Mr.Xu
Create:  2020/7/10 14:43
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""

"""
Author:  Mr.Xu
Create:  2020/7/10 14:10
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""

from randomList import randomList
from typing import *
ilist = randomList.randomList(20)


def selectionSort(l: List[int]):
    if len(l) <= 1:
        return l
    for i in range(len(l) - 1):
        minindex = i
        for j in range(i + 1, len(l)):
            if l[j] < l[minindex]:
                minindex = j
        l[i], l[minindex] = l[minindex], l[i]
        print("第{}轮排序结果:".format(i), end=" ")
        print(l)
    return l


if __name__ == '__main__':
    print(ilist)
    print(selectionSort(ilist))
