import sys

N = int(sys.stdin.readline())

memo = []

for i in range(1,N+1):
    a = ""
    a += ' ' * (N-i)
    a += '*' * (2*i-1)
    memo.append(a)
    print(a)

memo.pop()
for i in memo[::-1]:
    print(i)