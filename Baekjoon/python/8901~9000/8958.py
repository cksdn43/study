# ox퀴즈
n = int(input())
for _ in range(n):
    answer = input()
    score = 0
    result = 0
    for a in answer:
        if a == "O":
            score += 1
        else:
            score = 0
        result += score
    print(result)
