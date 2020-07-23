class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def pre_order(node: Node):
    stack = []
    while node or len(stack) > 0:
        while node:
            stack.append(node)
            print(node.data, end=" ")
            node = node.left
        if len(stack) > 0:
            node = stack.pop()
            node = node.right

def post_order(node: Node):
    stack1 = []
    stack2 = []
    stack1.append(node)
    while stack1:
        node = stack1.pop()
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
        stack2.append(node)
    while stack2:
        print(stack2.pop().data, end=' ')

def level_order(root: Node):
    from queue import Queue
    queue = Queue()
    queue.put(root)
    while not queue.empty():
        node = queue.get()
        print(node.data, end=' ')
        if node.left:
            queue.put(node.left)
        if node.right:
            queue.put(node.right)

if __name__ == '__main__':
    node1 = Node(4)
    node2 = Node(3)
    node3 = Node(1)
    node4 = Node(8)
    node1.left = node2
    node1.right = node4
    node2.left = node3
    pre_order(node1)
    print()
    post_order(node1)
    print()
    level_order(node1)
