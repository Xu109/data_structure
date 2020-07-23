"""
Author:  Mr.Xu
Create:  2020/7/15 12:38
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""

from randomList import randomList
from typing import *
ilist = randomList.randomList(20)

def mergeSort(iList: List):
    if len(iList) <= 1:
        return iList
    middle = len(iList)//2
    left, right = iList[:middle], iList[middle:]
    return merge1(mergeSort(left), mergeSort(right))

def merge(left: List, right: List):
    mList = []
    while left and right:
        if left[0] >= right[0]:
            mList.append(right.pop(0))
        else:
            mList.append(left.pop(0))
    while left:
        mList.append(left.pop(0))
    while right:
        mList.append(right.pop(0))
    return mList

def merge1(left: List, right: List):
    left_len = len(left)
    right_len = len(right)
    mList = []
    i = 0
    j = 0
    while i < left_len and j < right_len:
        if left[i] <= right[j]:
            mList.append(left[i])
            i += 1
        else:
            mList.append(right[j])
            j += 1
    while i < left_len:
        mList.append(left[i])
        i += 1
    while j < right_len:
        mList.append(right[j])
        j += 1
    return mList

if __name__ == '__main__':
    print(ilist)
    res = mergeSort(ilist)
    print(res)
