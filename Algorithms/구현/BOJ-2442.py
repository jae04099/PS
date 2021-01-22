n = int(input())
star = '*'
blank = ' '
stars = 1

for i in range(n, 0, -1):
    print(blank * (i - 1) + stars * star)
    stars += 2