N, M = tuple(map(int, input().split()))
x, y, way = tuple(map(int, input().split()))
map = [list(map(int, input().split())) for _ in range(M)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ways = [0, 1, 2, 3]

cnt = 1
key = 0

map[x][y] = 2

while 1:
    way -= 1
    key+=1
    if way < 0:
        way = 3
    tx = x + dx[way]
    ty = y + dy[way]
    if map[tx][ty] == 0:
        map[tx][ty] = 2
        x = tx
        y = ty
        cnt += 1
        key = 0
    if key >= 4:
        break
print(cnt)