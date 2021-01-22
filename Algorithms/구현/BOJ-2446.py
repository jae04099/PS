n = int(input())
star = '*'
space = ' '

for i in range(0, n):
    print(space * i, end='')
    print(star * (n-i), end='')
    print(star * (n - i - 1))
for i in range(n-1 , 0, -1):
    print(space * (i - 1), end='')
    print(star * (n - i ), end='')
    print(star * (n - (i - 1)))
