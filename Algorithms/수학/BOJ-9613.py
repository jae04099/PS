from itertools import combinations

def gcd(x, y):
    while y:
        x, y = y, (x % y)
    return x

n = int(input())
lists = []
result = 0
for _ in range(n):
    lists = list(map(int, input().split()))
    lists = lists[::-1]
    del lists[len(lists) - 1]
    ncr = combinations(lists, 2)
    for i in ncr:
        result += gcd(i[0], i[1])
    print(result)
    result = 0