
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        elif value > self.data:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
        else:
            self.data = value

    def inOrder(self):
        if self.left is not None:
            self.left.inOrder()
        print(self.data)
        if self.right is not None:
            self.right.inOrder()

    def preOrder(self):
        print(self.data)
        if self.left is not None:
            self.left.preOrder()
        if self.right is not None:
            self.right.preOrder()

    def postOrder(self):
        if self.left is not None:
            self.left.postOrder()
        if self.right is not None:
            self.right.postOrder()
        print(self.data)

if __name__ == "__main__":
    char = None
    root = Node(4)
    root.insert(3)
    root.insert(6)
    root.insert(2)
    root.insert(1)
    root.insert(5)
    root.insert(7)
    root.insert(8)

    print("inOrder traversal:")
    root.inOrder()
    print("preOrder traversal:")
    root.preOrder()
    print("PostOrder traversal:")
    root.postOrder()

