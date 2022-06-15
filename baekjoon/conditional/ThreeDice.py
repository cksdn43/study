a = input().split()
if a[0] == a[1] = a[2]:
  b = int(a[0])
  r = 10000 + b * 1000
elif a[0] == a[1]:
  b = int(a[0])
  r = 1000 + b * 100
 elif a[1] == a[2]:
  b = int(a[1])
  r = 1000 + b * 100
 elif a[0] == a[2]:
  b = int(a[2])
  r = 1000 + b * 100
 else:
  r = 1000 + max(a[0],a[1],a[3]) * 100

print(r)
  
