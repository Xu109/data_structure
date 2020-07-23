"""
Author:  Mr.Xu
Create:  2020/7/7 19:14
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""


from typing import List


class TrieNode:
    def __init__(self):
        self.data = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            child = node.data.get(char)
            if child is None:
                node.data[char] = TrieNode()
            node = node.data[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            node = node.data.get(char)
            if node is None:
                return False
        return node.is_word

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            node = node.data[char].get(char)
            if node is None:
                return False
        return True


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    # def __repr__(self):
    #     return f"{self.data}:({self.left},{self.right})"


def pre_order(node: Node):
    if node is None:
        return
    print(node.data, end=" ")
    pre_order(node.left)
    pre_order(node.right)
    return node


def in_order_stack(node: Node):
    stack = []
    while node or len(stack) > 0:
        while node:
            stack.append(node)
            node = node.left
        if len(stack) > 0:
            node = stack.pop()
            print(node.data, end=" ")
            node = node.right


def one_times(num: int):
    count = 0
    while num != 0:
        num = num & (num - 1)
        count += 1
    return count
def remove_val(nums: List, val: int):
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
        else:
            fast += 1
    return slow
if __name__ == '__main__':
    print(one_times(8))
    a = [1, 2, 3, 3, 5, 6, 7]
    b = remove_val(a, 3)
    print(a[:b])
