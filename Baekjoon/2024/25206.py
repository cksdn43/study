import sys

d = 0
e = 0

f = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0": 1.0, "F":0.0}

for _ in range(20):
    a, b, c = sys.stdin.readline().strip().split(" ")
    b = float(b)
    if(c == "P"):
        continue
    g = f[c]
    d += b
    e += (b*g)

print("%.6f"%(e / d))