n = int(input())

d = [0] * 12
d[1] = 1
d[2] = 2
d[3] = 4

def dp(x):
    global d
    for i in range(4, x + 1):
        d[i] = d[i - 1] + d[i - 2] + d[i - 3]
    return d[x]

for i in range(n):
    x = int(input())
    print(dp(x))