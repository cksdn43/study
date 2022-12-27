import random

quiz = {}
with open("codeit/data/vocabulary.txt", "r", encoding='UTF-8') as test:
    for words in test:
        word = words.strip().split(":")
        word[1] = word[1].strip()
        quiz[word[0]] = word[1]

print(quiz)
while 1:
    cor = random.choice(list(quiz.keys()))
    answer = input(f"{cor}: ")
    if answer == 'q':
        break
    elif answer == quiz[cor]:
        print("맞았습니다!")
    else:
        print(f"아쉽습니다. 정답은 {quiz[cor]}입니다.")