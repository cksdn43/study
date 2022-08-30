class Node:
    def __init__(self, element):
        self.data = element
        self.link = None


class linkedList:
    def __init__(self):
        self.head = None

    def getNode(self, pos):
        if pos < 0:
            return None
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
            return node

    def find(self, item):
        pos = 0
        current = self.head
        while current != None:
            if current.data == item:
                return pos
            else:
                current = current.link
        return

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.link
        return count

    def printList(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.link
        return
