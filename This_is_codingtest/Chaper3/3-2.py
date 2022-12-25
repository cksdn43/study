N, M, K = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()

result = 0

for m in range(1, M+1):
    if m % K == 0:
        result += arr[-2]
    else:
        result += arr[-1]
print(result)
