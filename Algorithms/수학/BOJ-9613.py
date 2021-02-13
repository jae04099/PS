# from itertools import combinations

# def gcd(x, y):
#     while y:
#         x, y = y, (x % y)
#     return x

# n = int(input())
# lists = []
# result = 0
# for _ in range(n):
#     lists = list(map(int, input().split()))
#     lists = lists[::-1]
#     del lists[len(lists) - 1]
#     ncr = combinations(lists, 2)
#     for i in ncr:
#         result += gcd(i[0], i[1])
#     print(result)
#     result = 0

from itertools import combinations

def GCD(x, y):
    while y:
        x, y = y, (x % y)
    return x
lists = []
result = 0


n = int(input())
for i in range(n):
    lists = list(map(int, input().split()))
    del lists[0]
    lists = lists[::-1]
    ncr = list(combinations(lists, 2))
    for i in ncr:
        result += GCD(i[0], i[1])
    print(result)
    result = 0
