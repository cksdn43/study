def count_matching_numbers(numbers, winning_numbers):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
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


# 테스트 코드
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))