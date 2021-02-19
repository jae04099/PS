#탑다운
d = [0] * 100


def fibo(x):
    if x == 1 or x == 2:
        return 1
    elif d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

#보텀업
d = [0] * 100
d[1] = 1
d[2] = 2

for i in range(3, n + 1):
    d[n] = d[n - 1] + d[n - 2]
print(d[99])