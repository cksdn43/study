class Node:
    def __init__(self, element):
        self.data = element
        self.link = None


class LinkedQueue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    def enqueue(self, e):
        newNode = Node(e)
        if self.front == None:
            self.front = self.rear = newNode
        else:
            self.rear.link = newNode
            self.rear = newNode

    def dequeue(self):
        if self.isEmpty():
            print("Queue empty")
            return
        e = self.front.data
        self.front = self.front.link
        if self.front == None:
            self.rear = None

        return e
