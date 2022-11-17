# 최댓값

A = [list(map(int, input().split()))for _ in range(9)]
result = 0

for i in range(9):
    a = max(A[i])
    if a >= result:
        result = a
        b = i
for i in range(9):
    if A[b][i] == result:
        c = i

print(result)
print(b+1, c+1)
