from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    if node is None:
        raise EOFError("List is empty")

    current = node
    count = 0

    while current:
        if count == index:
            return current
        current = current.next
        count += 1

    raise IndexError("Index out of bounds")

  