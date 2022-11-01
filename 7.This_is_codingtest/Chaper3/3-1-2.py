money = int(input())

coins = [500, 100, 50, 10]

cnt = money // coins[-1]

for i in range(len(coins)-1):
    result = 0
    n = money
    for j in range(i, len(coins)):
        result += n // coins[j]
        n %= coins[j]
    if cnt > result:
        cnt = result
print(cnt)
