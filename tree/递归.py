"""
Author:  Mr.Xu
Create:  2020/7/3 11:49
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""

import time

start = time.time()
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)
result = fib(4)
end = time.time()
print(end - start)
print(result)