# 주사위 세개
a, b, c = tuple(map(int, input().split()))

if a == b and b == c:
    print(10000+a*1000)
elif a != b and b != c and a != c:
    print(max(a, b, c)*100)
else:
    if b == c:
        print(1000+b*100)
    else:
        print(1000+a*100)
