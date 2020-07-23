"""
Author:  Mr.Xu
Create:  2020/7/15 19:07
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""


def greatest_common_factor(num1: int, num2: int) -> int:
    if num1 == num2:
        return num1
    elif num1 < num2:
        result = num1
    else:
        result = num2
    while result >= 1:
        if num1 % result == 0 and num2 % result == 0:
            print("{}和{}的最大公约数为:".format(num1, num2), result)
            return result
        else:
            result -= 1


#  暴力枚举法
def greatest_common_factor1(a: int, b: int) -> int:
    big = max(a, b)
    small = min(a, b)
    if big % small == 0:
        return small
    for i in range(small // 2, 0, -1):
        if big % i == 0 and small % i == 0:
            return i

#  辗转相除法(欧基米德)
def greatest_common_factor2(a: int, b: int) -> int:
    big = max(a, b)
    small = min(a, b)
    if big % small == 0:
        return small
    return greatest_common_factor2(small, big % small)

#  更相减损术
def greatest_common_factor3(a: int, b: int) -> int:
    if a - b == 0:
        return a
    big = max(a, b)
    small = min(a, b)
    return greatest_common_factor3(big - small, small)

if __name__ == '__main__':
    print(greatest_common_factor1(12, 15))
    print(greatest_common_factor3(12, 60))
    print(greatest_common_factor2(16, 20))
    print(greatest_common_factor1(13, 14))
