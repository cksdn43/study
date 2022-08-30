class DNode:
    def __init__(self, e):
        self.addr = e
        self.next = None
        self.back = None


class DlinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode, location):
        newNode.back = location.back
        newNode.next = location
        if location.back == None:
            self.head = newNode
        else:
            location.back.next = newNode
        location.back = newNode

    def delete(self, location):
        if location.back == None:
            self.head = location.next
            if location.next != None:
                location.next.back = None
        else:
            location.back.next = location.next
            if location.next != None:
                location.next.back = location.back
