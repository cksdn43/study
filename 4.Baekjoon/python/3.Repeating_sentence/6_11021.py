# A + B - 7
import sys

n = int(sys.stdin.readline())

for i in range(n):
    a, b = tuple(map(int, sys.stdin.readline().split(" ")))
    print(f"Case #{i+1}: {a+b}")
