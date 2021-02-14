from itertools import permutations

n = int(input())
lists = list(map(int, input().split()))
pers = list(permutations(lists, n))
res = []
num = 0

for i in pers:
    for j in range(n - 1):
        num += abs(i[j] - i[j + 1])
    res.append(num)
    num = 0
res = sorted(res)
print(res[len(res) - 1])
