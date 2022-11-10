# 더하기 사이클
L = []

N = input()

if int(N) < 10:
    N = "0" + N
L.append(N)

a = N[0]
b = N[1]

n = str(int(a)+int(b))
N = b + n[-1]
cnt = 1

while True:
    if N in L:
        break
    else:
        L.append(N)
    a = b
    b = N[-1]
    n = str(int(a)+int(b))
    N = b + n[-1]
    cnt += 1
print(cnt)
