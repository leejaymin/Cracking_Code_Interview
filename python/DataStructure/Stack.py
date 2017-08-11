
class Stack:
    def __init__(self):
        self.data = []

    # for print
    def __iter__(self):
        return self

    def __str__(self):
        values = [x for x in self]
        return ' -> '.join(values)

    def push(self, data):
        self.data.append(data)

    def pop(self):
        if len(self.data) is not 0:
            return self.data.pop()
        else:
            print("stack is empty")

    def print_stack(self):
        print(self.data)

if __name__ == "__main__":

    myStack = Stack()
    myStack.push(1)
    myStack.push(2)
    myStack.push(3)
    myStack.push(4)
    myStack.print_stack()

    print(myStack.pop())
    print(myStack.pop())

    myStack.print_stack()
