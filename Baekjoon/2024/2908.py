S = input().split()
a = int(S[0][::-1])
b = int(S[1][::-1])
print(a if a>b else b)