while 1:
    eng = input("영어 단어를 입력하세요: ")
    if eng == "q":
        break
    kor = input("한국어 뜻을 입력하세요: ")
    if kor == "q":
        break
    with open("codeit/data/vocabulary.txt","a",encoding='UTF8') as f:
        f.write(f"{eng}: {kor}\n")
