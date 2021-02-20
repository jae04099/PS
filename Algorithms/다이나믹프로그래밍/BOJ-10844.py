n = int(input())
d = [0] * (10 ** n)


def stair(x):
    x = str(x)
    for i in range(1, len(x)):
        if abs(int(x[i - 1]) - int(x[i])) == 1:
            return True


if n == 1:
    print(9)
else:
    for i in range(10 ** (n - 1), 10 ** n):
        if stair(i):
            d[i] = d[i - 1] + 1
        else:
            d[i] = d[i - 1]

    print(d[(10 ** n) - 1] % 1000000000)
