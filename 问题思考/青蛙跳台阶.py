"""
Author:  Mr.Xu
Create:  2020/7/3 15:29
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""
'''
一只青蛙可以一次跳 1 级台阶或一次跳 2 级台阶,例如:
跳上第 1 级台阶只有一种跳法：直接跳 1 级即可。跳上第 2 级台阶
有两种跳法：每次跳 1 级，跳两次；或者一次跳 2 级。
问要跳上第 n 级台阶有多少种跳法？
'''
# 第一步只能跳1步或者2步,剩下的就是n-1阶的步数,还有n-2阶的部署,两者相加就是n阶的步数


def frogs(n):
    if n > 2:
        return frogs(n - 1) + frogs(n - 2)
    if n == 1 or n == 2:
        return n

