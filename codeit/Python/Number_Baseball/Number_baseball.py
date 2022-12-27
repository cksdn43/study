from random import randint


def generate_numbers():
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    numbers = []
    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

def take_guess():
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    cnt = 1
    while cnt <= 3:
        n = int(input(f"{cnt}번째 숫자를 입력하세요: "))
        if n < 0 or n > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif n not in new_guess:
            new_guess.append(n)
            cnt+= 1
        else:
            print("중복되는 숫자입니다. 다시 입력하세요.")
    return new_guess

def get_score(guesses, solution):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    strike_count = 0
    ball_count = 0

    for i in range(len(solution)):
        if guesses[i] == solution[i]:
            strike_count += 1
        elif guesses[i] in solution:
            ball_count += 1

    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

# 여기에 코드를 작성하세요
while 1:
    tries +=1
    game = take_guess()
    strike, ball = get_score(game, ANSWER)
    print(f"{strike}S {ball}B")
    if strike == 3 and ball == 0:
        break

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
