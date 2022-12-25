dx = [1, -1, 0, 0] # 오 왼 위 아
dy = [0, 0, -1, 1]

n = int(input())

command = list(map(str, input().split()))

cx = 1
cy = 1

for c in command:
    if c == "R" and cx < n:
        cx += dx[0]
    elif c == "L" and cx > 1:
        cx += dx[1]
    elif c == "U" and cy > 1:
        cy += dy[2]
    elif c == "D" and cy < n:
        cy += dy[3]

print(cy, cx)