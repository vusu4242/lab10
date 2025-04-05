class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError("List must have at least two nodes.")
    head1 = head
    head2 = head.next
    current1 = head1
    current2 = head2
    current = head.next.next
    toggle = True
    while current:
        if toggle:
            current1.next = current
            current1 = current1.next
        else:
            current2.next = current
            current2 = current2.next
        toggle = not toggle
        current = current.next
    current1.next = None
    current2.next = None

    return Context(head1, head2)