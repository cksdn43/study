# 킹, 퀸, 룩, 비숍, 나이트, 폰
Pieces = [1, 1, 2, 2, 2, 8]
T = list(map(int, input().split()))

for i in range(len(Pieces)):
    T[i] = Pieces[i] - T[i]

for t in T:
    print(t, end=" ")
