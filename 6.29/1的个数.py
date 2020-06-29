"""
Author:  Mr.Xu
Create:  2020/6/29 9:28
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""
def hamingWeight(n):
    count = 0
    while n != 0:
        n = n & (n - 1)
        count += 1
    return count

