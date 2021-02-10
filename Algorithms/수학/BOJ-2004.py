#     n!
# ----------
# (n - r)!r!
from math import factorial
n, r = (map(int, input().split()))
pac = factorial(int(n)) // (factorial(int(n - r)) * factorial(int(r)))
count = 0

pac = str(pac)

for i in range(len(pac) - 1, 0, -1):
    if pac[i] == '0':
        count += 1
    else:
        break
print(count)

def factorials(x, y):
    