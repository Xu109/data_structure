"""
Author:  Mr.Xu
Create:  2020/7/16 12:25
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""

from randomList import randomList
ilist = randomList.randomList(20)


def swap(array, a, b):
    array[a], array[b] = array[b], array[a]


def partition(iList, start, end):
    pivot = iList[start]
    p = start + 1
    q = end  # 47653281
    while p <= q:
        while p <= q and iList[p] < pivot:
            p += 1
        while p <= q and iList[q] >= pivot:
            q -= 1
        if p < q:
            swap(iList, p, q)
    swap(iList, start, q)
    return q


def quickSort(iList, start, end):
    if start >= end:
        return
    mid = partition(iList, start, end)
    quickSort(iList, start, mid - 1)
    quickSort(iList, mid + 1, end)


if __name__ == '__main__':
    print(ilist)
    quickSort(ilist, 0, len(ilist) - 1)
    print(ilist)
