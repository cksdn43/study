import sys

n = int(sys.stdin.readline())

def check(word):
    letter = []
    current = word[0]
    letter.append(word[0])
    for w in word:
        if (current == w):
            continue
        elif (w not in letter):
            letter.append(w)
            current = w
        else:
            return False
    return True    

count = 0


for i in range(n):
    word = sys.stdin.readline()
    if (check(word)):
        count += 1

print(count)