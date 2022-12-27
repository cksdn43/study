import random

# 여기에 코드를 작성하세요
result = random.randint(1, 20)
cor = False
for i in range(4, 0, -1):
    answer = int(input(f"기회가 {i}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: "))
    if answer == result:
        cor = True
        a = 5 - i
        break
    elif answer > result:
        print("Down")
    else:
        print("UP")
if cor == False:
    print(f"아쉽습니다. 정답은 {result}였습니다.")
else:
    print(f"축하합니다. {a}번만에 숫자를 맞히셨습니다.")