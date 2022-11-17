# 나머지
import sys
A = [int(sys.stdin.readline().strip()) for _ in range(10)]
B = []

for a in A:
    if a % 42 not in B:
        B.append(a % 42)

print(len(B))
