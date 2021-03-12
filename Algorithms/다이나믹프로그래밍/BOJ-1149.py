n = int(input())
lists = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    lists[i][0] = min(lists[i - 1][1], lists[i - 1][2]) + lists[i][0]
    lists[i][1] = min(lists[i - 1][0], lists[i - 1][2]) + lists[i][1]
    lists[i][2] = min(lists[i - 1][1], lists[i - 1][0]) + lists[i][2]
result = min(lists[n - 1][0], lists[n - 1][1], lists[n - 1][2])
print(result)