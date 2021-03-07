n = int(input())
lists = [0] * 301
dp = [0] * 301
for i in range(n):
    lists[i] = int(input())

dp[0] = lists[0]
dp[1] = lists[0] + lists[1]
dp[2] = max(lists[1] + lists[2], lists[0] + lists[2])

for i in range(3, n):
    dp[i] = max(dp[i - 3] + lists[i - 1] + lists[i], dp[i - 2] + lists[i])
print(dp[n - 1])