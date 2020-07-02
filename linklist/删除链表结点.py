from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


def remove1(head: Optional[Node], val: int):
    dummy = Node(0)
    dummy.next = head
    curr = dummy
    while curr.next:
        if curr.next.data == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next


def remove(head: Optional[Node], val: int):
    if head is None:
        raise Exception("空链表!")
    while True:
        if head.data == val:
            head = head.next
        else:
            break
    curr = head
    while curr.next:
        if curr.next.data != val:
            curr = curr.next
        else:
            curr.next = curr.next.next
            curr = curr.next
    return head


def print_list(head: Optional[Node]):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    print(print_list(remove1(node1, 1)))

