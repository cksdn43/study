# 평균은 넘겠지
n = int(input())
for _ in range(n):
    L = list(map(int, input().split()))
    a = 0
    average = (sum(L) - L[0])/L[0]
    for l in L[1:]:
        if average < l:
            a += 1
    print(f"{a/L[0]*100:.3f}%")
