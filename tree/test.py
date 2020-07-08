"""
Author:  Mr.Xu
Create:  2020/7/7 19:14
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""

# class TrieNode:
#     def __init__(self):
#         self.data = {}
#         self.is_word = False
#
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self, word):
#         node = self.root
#         for char in word:
#             child = node.data.get(char)
#             if child is None:
#                 node.data[char] = TrieNode()
#             node = node.data[char]
#         node.is_word = True
#
#     def search(self, word):
#         node = self.root
#         for char in word:
#             node = node.data.get(char)
#             if node is None:
#                 return False
#         return node.is_word
#
#     def startsWith(self, prefix):
#         node = self.root
#         for char in prefix:
#             node = node.data.get(char)
#             if not node:
#                 return False
#         return True


# class TrieNode:
#     def __init__(self):
#         self.data = {}
#         self.is_word = False
#
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self, word):
#         node = self.root
#         for char in word:
#             child = node.data.get(char)
#             if not child:
#                 node.data[char] = TrieNode()
#             node = node.data[char]
#         node.is_word = True
#
#     def search(self, word):
#         node = self.root
#         for char in word:
#             node = node.data.get(char)
#             if not node:
#                 return False
#         return node.is_word
#
#     def startsWith(self, prefix):
#         node = self.root
#         for char in prefix:
#             node = node.data.get(char)
#             if not node:
#                 return False
#         return True


# class TrieNode:
#     def __init__(self):
#         self.data = {}
#         self.is_word = False
#
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self, word):
#         node = self.root
#         for char in word:
#             child = node.data.get(char)
#             if not child:
#                 node.data[char] = TrieNode()
#             node = node.data[char]
#         node.is_word = True
#
#     def search(self, word):
#         node = self.root
#         for char in word:
#             node = node.data.get(char)
#             if not node:
#                 return False
#         return node.is_word
#
#     def startsWith(self, prefix):
#         node = self.root
#         for char in prefix:
#             node = node.data.get(char)
#             if not node:
#                 return False
#         return True
#
# if __name__ == '__main__':
#     t = Trie()
#     t.insert('test')
#     print(t.search('test'))
#     print(t.search('tests'))
#     print(t.startsWith('te'))
#     print(t.startsWith('tei'))


# class Node:
#     def __init__(self, value, parent):
#         self.value = value
#         self.parent = parent
#         self.left = None
#         self.right = None
#
#
# def preorder(node):
#     if node is None:
#         return
#     print(node.value, end=" ")
#     preorder(node.left)
#     preorder(node.right)
#     return node
#
# def inorder(node):
#     if node is None:
#         return
#     inorder(node.left)
#     print(node.value, end=" ")
#     inorder(node.right)
#     return node
#
# def postorder(node):
#     if node is None:
#         return
#     postorder(node.left)
#     postorder(node.right)
#     print(node.value, end=" ")
#     return node


# class Node:
#     def __init__(self, value, parent):
#         self.value = value
#         self.parent = parent
#         self.left = None
#         self.right = None
#
# def pre_order_stack(node):
#     stack = []
#     while node or len(stack) > 0:
#         while node:
#             print(node.value)
#             stack.append(node)
#             node = node.left
#         if len(stack) > 0:
#             node = stack.pop()
#             node = node.right
#
# def in_order_stack(node):
#     stack = []
#     while node and len(stack) > 0:
#         while node:
#             stack.append(node)
#             node = node.left
#         if len(stack) > 0:
#             node = stack.pop()
#             print(node.value)
#             node = node.right
#
# def post_order_stack(node):
#     stack1 = []
#     stack2 = []
#     stack1.append(node)
#     while stack1:
#         node = stack1.pop()
#         if node.left:
#             stack1.append(node.left)
#         if node.right:
#             stack1.append(node.right)
#         stack2.append(node)
#     while stack2:
#         print(stack2.pop().value, end=" ")



# class Node:
#     def __init__(self, value, parent):
#         self.value = value
#         self.parent = parent
#         self.left = None
#         self.right = None
#
# def pre_order_stack(node):
#     stack = []
#     while node or len(stack) > 0:
#         while node:
#             print(node.value)
#             stack.append(node)
#             node = node.left
#         if len(stack) > 0:
#             node = stack.pop()
#             node = node.right
#
# def in_order_stack(node):
#     stack = []
#     while node and len(stack) > 0:
#         while node:
#             stack.append(node)
#             node = node.left
#         if len(stack) > 0:
#             node = stack.pop()
#             print(node.value)
#             node = node.right
#
# def post_order_stack(node):
#     stack1 = []
#     stack2 = []
#     stack1.append(node)
#     while stack1:
#         node = stack1.pop()
#         if node.left:
#             stack1.append(node.left)
#         if node.right:
#             stack1.append(node.right)
#         stack2.append(node)
#     while stack2:
#         print(stack2.pop().value, end=" ")



# class Node:
#     def __init__(self, value, parent):
#         self.value = value
#         self.parent = parent
#         self.left = None
#         self.right = None
#
# def pre_order_stack(node):
#     stack = []
#     while node or len(stack) > 0:
#         while node:
#             print(node.value)
#             stack.append(node)
#             node = node.left
#         if len(stack) > 0:
#             node = stack.pop()
#             node = node.right
#
# def in_order_stack(node):
#     stack = []
#     while node and len(stack) > 0:
#         while node:
#             stack.append(node)
#             node = node.left
#         if len(stack) > 0:
#             node = stack.pop()
#             print(node.value)
#             node = node.right
#
# def post_order_stack(node):
#     stack1 = []
#     stack2 = []
#     stack1.append(node)
#     while stack1:
#         node = stack1.pop()
#         if node.left:
#             stack1.append(node.left)
#         if node.right:
#             stack1.append(node.right)
#         stack2.append(node)
#     while stack2:
#         print(stack2.pop().value, end=" ")



# class Node:
#     def __init__(self, value, parent):
#         self.value = value
#         self.parent = parent
#         self.left = None
#         self.right = None
#
# def pre_order_stack(node):
#     stack = []
#     while node or len(stack) > 0:
#         while node:
#             print(node.value)
#             stack.append(node)
#             node = node.left
#         if len(stack) > 0:
#             node = stack.pop()
#             node = node.right
#
# def in_order_stack(node):
#     stack = []
#     while node and len(stack) > 0:
#         while node:
#             stack.append(node)
#             node = node.left
#         if len(stack) > 0:
#             node = stack.pop()
#             print(node.value)
#             node = node.right
#
# def post_order_stack(node):
#     stack1 = []
#     stack2 = []
#     stack1.append(node)
#     while stack1:
#         node = stack1.pop()
#         if node.left:
#             stack1.append(node.left)
#         if node.right:
#             stack1.append(node.right)
#         stack2.append(node)
#     while stack2:
#         print(stack2.pop().value, end=" ")


# def pre_order_stack(node):
#     stack = []
#     while node or len(stack) > 0:
#         while node:
#             print(node.value)
#             stack.append(node)
#             node = node.left
#         if len(stack) > 0:
#             node = stack.pop()
#             node = node.right
#
# def in_order_stack(node):
#     stack = []
#     while node or len(stack) > 0:
#         while node:
#             stack.append(node)
#             node = node.left
#         if len(stack) > 0:
#             node = stack.pop()
#             print(node.value)
#             node = node.right
#
# def post_order_stack(node):
#     stack1 = []
#     stack2 = []
#     stack1.append(node)
#     while stack1:
#         node = stack1.pop()
#         if node.left:
#             stack1.append(node.left)
#         if node.right:
#             stack1.append(node.right)
#         stack2.append(node)
#     while stack2:
#         print(stack2.pop().value, end=" ")


# def level_order(root: Node):
#     from queue import Queue
#     queue = Queue()
#     queue.put(root)
#     while not queue.empty():
#         node = queue.get()
#         print(node.value, end=" ")
#         if node.left:
#             queue.put(node.left)
#         if node.right:
#             queue.put(node.right)


# def level_order(root: Node):
#     from queue import Queue
#     queue = Queue()
#     queue.put(root)
#     while not queue.empty():
#         node = queue.get()
#         print(node.value, end=" ")
#         if node.left:
#             queue.put(node.left)
#         if node.right:
#             queue.put(node.right)


# def level_order(root: Node):
#     from queue import Queue
#     queue = Queue()
#     queue.put(root)
#     while not queue.empty():
#         node = queue.get()
#         print(node.value, end=" ")
#         if node.left:
#             queue.put(node.left)
#         if node.right:
#             queue.put(node.right)


# def level_order(root: Node):
#     from queue import Queue
#     queue = Queue()
#     queue.put(root)
#     while not queue.empty():
#         node = queue.get()
#         print(node.value, end=" ")
#         if node.left:
#             queue.put(node.left)
#         if node.right:
#             queue.put(node.right)


