def push(head, data):
    head_ = Node(data)
    if not head:
        return head_
    head_.next = head
    return head_

def build_one_two_three():
    head = None
    for data in [3,2,1]:
        head = push(head, data)
    return head