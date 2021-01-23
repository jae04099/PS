n = int(input())
lists = list(map(int, input().split(' ')))

dps = [0] * 100

dps[0] = lists[0]
dps[1] = max(lists[0], lists[1])

for i in range(2, n):
    dps[i] = max(dps[i - 1], dps[i - 2] + lists[i])

print(dps[n - 1])