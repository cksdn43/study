avg = 0
cnt = 0

with open("codeit/data/chicken.txt", "r",encoding='UTF8') as f:
    for lines in f:
        line = lines.split(":")
        avg += int(line[1].strip())
        cnt += 1
print(avg/cnt)