# 최댓값
import sys

idx = 1
max_value = int(sys.stdin.readline())

for i in range(2, 10):
    v = int(sys.stdin.readline())
    if max_value < v:
        max_value = v
        idx = i

print(max_value)
print(idx)
