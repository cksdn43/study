a = input().split()
b = input()
a[0], a[1], b = int(a[0]), int(a[1]) int(b)
a[1] += b
if a[1] >= 60:
  a[1] -= 60
  a[0] += 1
print(a[0], a[1])
