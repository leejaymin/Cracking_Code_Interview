class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def endNode(head):
    if head.next:
        head = endNode(head.next)
    else:
        return head
    return head


def Insert(head, data):
    if head == None:
        return Node(data, None)

    lastHead = endNode(head)
    lastHead.next = Node(data, None)
    return head


def print_list(head):
    if head == None:
        return
    else:
        print(head.data)

    print_list(head.next)

if __name__ == "__main__":
    head = Insert(None,1)
    head = Insert(head,2)
    head = Insert(head, 3)
    print_list(head)