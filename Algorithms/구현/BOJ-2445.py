n = int(input())
star = '*'
space = ' '

for i in range(0, n):
    print(star * (i + 1) + space * (n - (i + 1)) + space * (n - (i + 1)) + star * (i + 1))

for i in range(n-1, 0, -1):
    print(star * i + space * (n - i) + space * (n - i) + star * i)