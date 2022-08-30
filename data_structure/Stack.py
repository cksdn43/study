class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):  # stack이 비었는지 확인
        return len(self.items) == 0

    def clear(self):  # stack 비우기
        self.items = []

    def push(self, e):  # 항목 삽입
        self.items.append(e)

    '''
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.items.pop()
    '''

    def pop(self):  # 항목 삭제
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def size(self):  # 항목 크기
        return len(self.items)

    '''
    def peek(self):
        if self.isEmpty():
            print("Stack is empty)
        else:
            return self.items[-1]
    '''

    def peek(self):
        try:
            return self.items[-1]  # return self.items[len(self.items)-1]
        except IndexError:
            print("Stack is empty")


s = Stack()

n = int(input())

while n != 0:
    s.push(n % 2)
    n //= 2

while not s.isEmpty():
    digit = s.pop()
    print(digit, end="'")
