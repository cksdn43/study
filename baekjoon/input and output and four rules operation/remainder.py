t = input().split()
a = t[0]
a = int(a)
b = t[1]
b = int(b)
c = t[2]
c = int(c)
print((a+b)%c)
print(((a%c)%(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)
