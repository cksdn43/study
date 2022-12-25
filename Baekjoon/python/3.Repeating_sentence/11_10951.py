import sys

while True:
    try:
        a, b = tuple(map(int, sys.stdin.readline().split(" ")))
        print(a+b)
    except:
        break
