# 영수증

X = int(input())
n = int(input())
Y = 0
for i in range(n):
    a, b = tuple(map(int, input().split()))
    Y += a * b
if Y == X:
    print("Yes")
else:
    print("No")
