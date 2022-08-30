class Node:
    def __init__(self, element):
        self.data = element
        self.link = None


class linkedList:
    def __init__(self):
        self.head = None

    def getNode(self, pos):
        return self.getNodeLinkedList(self.head, pos)

    def getNodeLinkedList(self, ptr, pos):
        if ptr == None or pos < 0:
            return
        elif pos == 0:
            return ptr
        else:
            return self.getNodeLinkedList(ptr.link, pos-1)

    def find(self, item):
        return self.findLinkedList(self.head, item)

    def findLinkedList(self, ptr, item):
        if ptr == None:
            return
        elif ptr.data == item:
            return 0
        else:
            pos = self.findLinkedList(ptr.link, item)
            if pos == -1:
                return -1
            else:
                return pos + 1

    def size(self):
        return self.sizeLinkedList(self.head)

    def sizeLinkedList(self, ptr):
        if ptr == None:
            return 0
        else:
            return self.sizeLinkedList(ptr.link) + 1

    def printList(self):
        return self.printLinkedList(self.head)

    def printLinkedList(self, ptr):
        if ptr != None:
            print(ptr.data)
            self.printLinkedList(ptr.link)
