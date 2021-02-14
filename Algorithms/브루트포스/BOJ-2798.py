import itertools
com = []
n, m = map(int, input().split())
cards = list(map(int, list(input().split(' '))))
plus = []

com = list(itertools.combinations(cards, 3))
for i in com:
    plusNum = i[0] + i[1] + i[2]
    if plusNum <= m:
        plus.append(plusNum)
        plusNum = 0
    else:
        plusNum = 0
plus = sorted(plus)
print(plus[len(plus) - 1])
