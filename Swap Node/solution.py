from preloaded import Node

def swap_pairs(head):
    node = Node(0)
    node.next = head
    previous = node
    while previous.next and previous.next.next:
        first = previous.next 
        second = previous.next.next
        first.next = second.next
        second.next = first
        previous.next = second
        previous = first
    
    return node.next