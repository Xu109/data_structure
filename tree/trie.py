"""
Author:  Mr.Xu
Create:  2020/7/7 14:41
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""

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
            if not child:
                node.data[char] = TrieNode()
            node = node.data[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            node = node.data.get(char)
            if not node:
                return False
        return node.is_word

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            node = node.data.get(char)
            if not node:
                return False
        return True
