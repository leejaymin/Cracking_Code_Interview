
class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, data=None):
        self.head = None
        self.tail = None
        if data is not None:
            self.insert(data)

    # for print
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def insert(self, data):
        if self.head is None:
            self.tail = self.head = Node(data)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        return self.tail

    def delete(self, data):
        if self.head is None:
            print("It is empty!")
            return
        elif self.head.data is data:
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not None:
                if current.data is data:
                    print("Delete the number: %d"%(data))
                    current.data = current.next.data
                    current.next = current.next.next
                    return
                current = current.next
            print("It is not founded")


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    print(ll)
    ll.delete(3)
    ll.delete(6)
    print(ll)
