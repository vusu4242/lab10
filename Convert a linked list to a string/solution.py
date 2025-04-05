'''Convert a linked list to a string'''
def stringify(node):
    '''Convert a linked list to a string'''
    nodes = []
    if node is None:
        return 'None'
    current = node
    while current:
        nodes.append(current)
        current = current.next
    return ' -> '.join(list(str(node.data) for node in nodes)+['None'])
