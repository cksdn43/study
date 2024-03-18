N = int(input())
A = list(map(int, input().split()))
B = sorted(A)
P = []


for i in range(N):
    for j in range(N):
        if A[i] == B[j] and j not in P:
            P.append(j)
            print(j, end=" ")
            break
