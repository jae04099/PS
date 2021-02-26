# n = int(input())
# d = [0] * (n)
# real = [list(map(int, input().split()))]

# for i in range(n):
#     for j in range(i):
#         if real[i] > real[j] and d[i] < d[j]:
# n가지 종류 화폐. m원이 되도록 하는 최소한의 갯수
n, m = map(int, input().split())
lists = [int(input()) for _ in range(n)]
dp =[10001] * (m + 1)

dp[0] = 0
for i in range(n):
    for j in range(dp[i], )