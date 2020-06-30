"""
Author:  Mr.Xu
Create:  2020/6/29 15:01
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""

"""
14 编写一个函数来查找字符串数组中的最长公共前缀。
链接：https://leetcode-cn.com/problems/longest-common-prefix

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

"""

# a = [1, 2, 3]
# b = [4, 5, 6]
# zipped = list(zip(a, b))
# print(zipped)
# for each in zipped:
#     print(each)
#
# for each in zip(*zipped):
#     print(each)
#
# strs = ["flower", "flow", "flight"]
# minLength = min([len(s) for s in strs])
# print(minLength)




from typing import List
def longestCommonPrefix(strs: List[str]):
    if len(strs) == 0 or "" in strs:  # 判断空字符串的特殊情况,返回""即可
        return ""
    if len(strs) == 1:  # 如果只有一个字符串,那公共前缀就是它本身
        return strs
    minLength = min([len(s) for s in strs])  # 设定一个最小长度,这个最小长度是strs里最短字符串的长度
    publicWord = []  # 预留出存储公共前缀的变量
    for i in range(minLength):  # i就循环到最小长度即可,因为是公共前缀,不可能比最小字符串长度还长
        for word in strs:
            # 将所有的字符串的当前长度头字符放入publicWord中,用来后面判断
            publicWord.append(word[:i + 1])
        if len(set(publicWord)) == 1:  # 如果len(set(publicWord)) == 1证明里面所有字符串当前前缀相同,为重复值
            publicWord = []  # 当前长度前缀已满足条件,但还有可能存在更长,将publicWord置空,留着后面继续判断
        else:  # 当前缀已经不同时,即没有更长的公共前缀,就返回上一次循环最终得到的前缀,用[0]取第一个字符串的即可,都一样
            return strs[0][:i]
        return strs[0][:i+1]


def longCommonPrefix(strs: List[str]):
    res = ''
    for each in zip(*strs):  # zip(*strs)里是strs里的每一个字符串的相同位,将它们挨个遍历
        if len(set(each)) == 1:  # 如果该组字符全部重复,即集合长度为1,则满足条件
            res += each[0]  # 如果前面相同,那结果加上该字符然后继续判断下一字符
        else:  # 如果当前字符已经不相同,那就直接返回结果,不加新字符
            return res
    return res


#
#
if __name__ == '__main__':
    l = ["c", "c"]
    print(longCommonPrefix(l))
    print(longestCommonPrefix(l))
