n = int(input())
star = '*'
blank = ' '

for i in range(0, n):
    print(i * blank + star * (n - i))