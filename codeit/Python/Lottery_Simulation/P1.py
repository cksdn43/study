from random import randint


def generate_numbers(n):
    numbers = []
    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)
    return numbers
    
win_numbers = generate_numbers(6)
print(win_numbers)