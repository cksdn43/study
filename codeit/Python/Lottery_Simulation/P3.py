def count_matching_numbers(numbers, winning_numbers):
    # 여기에 코드를 작성하세요
    cnt = 0
    for num in winning_numbers:
        if num in numbers:
            cnt += 1
    return cnt


# 테스트 코드
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))