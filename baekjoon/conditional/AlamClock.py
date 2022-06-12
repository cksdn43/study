time = input().split()
time[0], time[1]= int(time[0]), int(time[1])

if time[1] >= 60:
  time[0] += time[1] // 60
  time[1] %= 60
 
if time[0] >= 24:
  time[0] -= 24
 
time[1] -= 45

if time[1] < 0:
  time[0] -= 1
  time[1] += 60
if time[0] < 0:
  tiem[0] += 24

 print(time[0], time[1])

