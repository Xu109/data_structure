"""
Author:  Mr.Xu
Create:  2020/7/1 9:38
Github:  https://github.com/Xu109
Copyright (c) 2020, Mr.Xu Group All Rights Reserved.
"""
from pprint import pformat


class Node:
    def __init__(self, value, parent):
        self.value = value  # 表示对应的元素
        self.parent = parent
        self.left = None  # 表示左节点
        self.right = None  # 表示右节点

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({"%s" % (self.value): (self.left, self.right)}, indent=1)


class binary_search_tree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def is_empty(self):
        return self.root is None

    def is_right(self, node):
        return node == node.parent.right

    def __insert(self, value):
        new_node = Node(value, None)
        if self.is_empty():
            self.root = new_node
        else:
            parent_node = self.root
            while True:
                if value < parent_node.value:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break
                    else:
                        parent_node = parent_node.left
                elif value >= parent_node.value:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node = parent_node.right
            new_node.parent = parent_node

    def insert(self, *args):
        for value in args:
            self.__insert(value)
        return self

    def search(self, value):
        if self.is_empty():
            raise IndexError("空树查个啥劲")
        else:
            node = self.root
            while node and node.value != value:
                node = node.left if value < node.value else node.right
            print(node)
            return node

    def remove(self, value: int):
        search_node = self.search(value)
        if search_node:
            if search_node.left is None and search_node.right is None:
                self.__reassign_nodes(search_node, None)
            elif search_node.left is None:
                self.__reassign_nodes(search_node, search_node.right)
            elif search_node.right is None:
                self.__reassign_nodes(search_node, search_node.left)
            else:
                temp = self.get_max(search_node.left)
                self.remove(temp.value)
                search_node.value = temp.value

    def __reassign_nodes(self, node, new_chirdren):
        if new_chirdren:
            new_chirdren.parent = node.parent
        if node.parent:
            if self.is_right(node):
                node.parent.right = new_chirdren
            else:
                node.parent.left = new_chirdren
        else:
            self.root = new_chirdren

    def get_max(self, node=None):
        if node is None:
            node = self.root
        if not self.is_empty():
            while node.right:
                node = node.right
        return node

    def get_min(self, node=None):
        if node is None:
            node = self.root
        if not self.is_empty():
            while node.left:
                node = node.left
        return node

    def preorder(self, node):
        """self, left, right"""
        if node is None:
            return
        print(node.value, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)
        return node

    def inorder(self, node):
        """left,self,right"""
        if node is None:
            return
        self.inorder(node.left)
        print(node.value, end=" ")
        self.inorder(node.right)
        return node

    def postorder(self, node):
        """left, right, self"""
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value, end=" ")
        return node

if __name__ == '__main__':
    bst = binary_search_tree().insert(8, 3, 1, 6)
    print(bst)
    bst.preorder(bst.root)
    print()
    bst.inorder(bst.root)
    print()
    bst.postorder(bst.root)
