n = int(input())
result = 0
if n < 100:
    print(n)
elif 100 <= n:
    result = 99
    for i in range(100, n + 1):
        num = list(map(int, list(str(i))))
        if (num[0] - num[1]) == (num[1] - num[2]):
            result += 1
    print(result)
