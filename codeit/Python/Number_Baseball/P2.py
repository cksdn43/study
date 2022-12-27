def take_guess():
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
print(take_guess())