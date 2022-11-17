# X보다 작은 수
import sys

n, x = tuple(map(int, sys.stdin.readline().split()))
A = list(map(int, sys.stdin.readline().split()))

for a in A:
    if a < x:
        print(a, end=" ")
