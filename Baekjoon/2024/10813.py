# 변수 선언 및 입력
N, M = map(int, input().split())

# 바구니 생성
basket = [i for i in range(N+1)]

# 입력에 따라 공 교환
for _ in range(M):
    a, b = map(int, input().split())
    basket[a], basket[b] = basket[b], basket[a]

# 바구니에 있는 공출력
for i in basket[1:]:
    print(i, end=' ')
