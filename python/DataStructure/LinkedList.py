
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def Insert(head, data):
    if head == None:
        return Node(data, None)

    current = head
    # reach the last node
    while current.next != None:
        current = current.next

    current.next = Node(data, None)
    return head

def delete(head):
    if head == None:
        return "It is empty!"

    while head.next is not None:
        if head.next.next is None:
            head.next = None
            break
        head = head.next

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
    head = Insert(head, 4)
    delete(head)
    delete(head)
    head = Insert(head, 5)
    print_list(head)