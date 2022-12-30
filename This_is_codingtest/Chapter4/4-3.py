n = [[0 for _ in range(8)]for _ in range(8)]

move = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
c = input()

ch = ord(c[0]) - 97
cr = int(c[1])-1
cnt = 0

for m in move:
    fh = ch+m[0]
    fr = cr+m[1]
    try:
        a = n[fh][fr]
        if fh >= 0 and fr >= 0:
            cnt += 1
    except:
        pass
print(cnt)
