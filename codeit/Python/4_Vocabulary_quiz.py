with open("codeit/data/vocabulary.txt", "r", encoding='UTF-8') as test:
    for words in test:
        word = words.strip().split(":")
        answer = " " + input(f"{word[0]}: ")
        if answer == word[1]:
            print("맞았습니다!")
        else:
            print(f"아쉽습니다. 정답은{word[1]}입니다.")