class robot:
    def __init__(self):
        self.position = 1000
        self.load = [0] * 2001

    def Rmove(self, n - 1):
        for i in range(0, n):
            self.position += 1
            self.load[self.position] += 1

    def Lmove(self, n):
        for i in range(0, n):
            self.position -= 1
            self.load[self.position] += 1


r = robot()

n = int(input())
for i in range(n):
    x, c = input().split()
    x = int(x)
    if c == "R":
        r.Rmove(x)
    elif c == "L":
        r.Lmove(x)

result = 0

for i in r.load:
    if i >= 2:
        result += 1

print(result)
