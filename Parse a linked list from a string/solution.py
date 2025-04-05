'''Parse a linked list from a string'''
def linked_list_from_string(s):
    '''Parse a linked list from a string'''
    nodes = s.split(' -> ')[:-1]
    head = None
    for data in reversed(nodes):
        head = Node(int(data), head)
    return head
