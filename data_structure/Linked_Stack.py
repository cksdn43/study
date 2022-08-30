class Node:
    def __init__(self, element):
        self.data = element
        self.link = None


class LinkedStack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None

    def push(self, e):
        newNode = Node(e)
        newNode.link = self.top
        self.top = newNode

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        e = self.top.data
        self.top = self.top.link
        return e
