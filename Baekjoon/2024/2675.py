T = int(input())
for _ in range(T):
    R, S = input().split()
    for j in S:
        for i in range(int(R)):
            print(j, end='')
