# 최대, 최소
import sys

n = sys.stdin.readline()

L = list(map(int, sys.stdin.readline().split()))

minvalue = L[0]
maxvalue = L[0]

for l in L:
    if maxvalue < l:
        maxvalue = l
    if minvalue > l:
        minvalue = l
print(minvalue, maxvalue)
