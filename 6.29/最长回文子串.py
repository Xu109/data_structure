"""
Author:  Mr.Xu
Create:  2020/6/29 11:54
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""


def longestPalindrome(strs: str):
    length = len(strs)
    if length < 2:
        return strs
    maxlen = 1
    res = strs[0]
    for i in range(length - 1):
        odd = centerSpread(strs, i, i)
        even = centerSpread(strs, i, i + 1)
        maxstr = odd if len(odd) > len(even) else even
        if len(maxstr) > maxlen:
            maxlen = len(maxstr)
            res = maxstr
    return res


def centerSpread(strs: str, left: int, right: int):
    length = len(strs)
    i = left
    j = right
    while i >= 0 and j < length:
        if strs[i] == strs[j]:
            i -= 1
            j += 1
        else:
            break
    return strs[i + 1:j]
