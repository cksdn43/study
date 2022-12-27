from random import randint

def generate_numbers(n):
    numbers = []
    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)
    return numbers

def count_matching_numbers(numbers, winning_numbers):
    # 여기에 코드를 작성하세요
    cnt = 0
    for num in winning_numbers:
        if num in numbers:
            cnt += 1
    return cnt

def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]

def count_matching_numbers(numbers, winning_numbers):
    # 여기에 코드를 작성하세요
    cnt = 0
    for num in winning_numbers:
        if num in numbers:
            cnt += 1
    return cnt

def check(numbers, winning_numbers):
    # 여기에 코드를 작성하세요
    same_cnt = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_cnt = count_matching_numbers(numbers, winning_numbers[6:])
    if same_cnt == 6:
        return 100000000
    elif same_cnt == 5 and bonus_cnt == 1:
        return 50000000
    elif same_cnt == 5:
        return 1000000
    elif same_cnt == 4:
        return 50000
    elif same_cnt == 3:
        return 5000
    else:
        return 0
