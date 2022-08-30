import time

myBag = []
start = time.time()
myBag.append('축구공')
for i in myBag:
    print(i)
end = time.time()
print("실행시간 = ", end-start)
