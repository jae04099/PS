import itertools
height = list(int(input()) for _ in range(9))
height = sorted(height)
res = []

heights = itertools.combinations(height, 7)
for i in heights:
    if sum(i) == 100:
        res.append(i)
for i in range(7):
    print(res[0][i])

