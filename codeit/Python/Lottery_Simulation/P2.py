from random import randint


def generate_numbers(n):
    numbers = []
    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)
    return numbers


def draw_winning_numbers():
    """ game_numbers = sorted(generate_numbers(6))
    while len(game_numbers) < 7:
        num = randint(1, 45)
        if num not in game_numbers:
            game_numbers.append(num)
    return game_numbers """
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]


game_numbers = draw_winning_numbers()
print(game_numbers)