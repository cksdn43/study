money = int(input())

coins = [500, 100, 50, 10]

cnt = 0

for coin in coins:
    cnt += money // coin
    money %= coin

print(cnt)
