# 변수 선언 및 입력
N, M = map(int, input().split())

# 바구니 생성
basket = [i for i in range(N+1)]

# 입력에 따라 범위 뒤집기
for _ in range(M):
    a, b = map(int, input().split())
    c = reversed(basket[a:b+1])
    for i in c:
        basket[a] = i
        a += 1

# 바구니에 있는 공출력
for i in basket[1:]:
    print(i, end=' ')