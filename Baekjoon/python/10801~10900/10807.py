# 개수 세기
n = input()
L = list(map(int, input().split()))
v = int(input())
cnt = 0

for i in L:
    if i == v:
        cnt += 1

print(cnt)
