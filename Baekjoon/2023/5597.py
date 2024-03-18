# 과제 안 내신 분..?

s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
     17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
o = []
x = []
for i in range(28):
    a = int(input())
    o.append(a)
for i in s:
    if i not in o:
        x.append(i)

if x[0] > x[1]:
    print(x[1])
    print(x[0])
else:
    print(x[0])
    print(x[1])
