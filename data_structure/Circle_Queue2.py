class Queue:
    MAX_QSIZE = 100  # 큐에 대한 크기 설정

    def __init__(self):
        self.items = [None]*Queue.MAX_QSIZE
        self.front = 0
        self.rear = 0
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, e):
        if self.size == len(self.items):
            print("Queue is Full")
            # self.resize(2*len(self.items))
        else:
            self.items[self.rear] = e
            self.rear = (self.rear + 1) % (len(self.items))
            self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            e = self.items[self.front]
            self.front = (self.front+1) % (len(self.items))
            self.size -= 1
            return e

    def resize(self, cap):
        olditems = self.items
        self.items = [None]*cap
        walk = self.front
        for k in range(self.size):
            self.items[k] = olditems[walk]
            walk = (walk + 1) % len(olditems)
        self.front = 0
        self.rear = self.size


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
e = q.dequeue()
print(e)
q.enqueue(40)
