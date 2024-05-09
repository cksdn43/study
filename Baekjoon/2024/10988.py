import sys

key = 1

string = sys.stdin.readline().strip()

n = len(string)

for i in range(n):
    if(string[i] != string[n-i-1]):
        key = 0
        break
    
print(key)