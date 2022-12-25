# A + B - 5
import sys

while True:
    a, b = tuple(map(int, sys.stdin.readline().split(" ")))
    if a == 0 and b == 0:
        break
    print(a+b)
