# n = int(input())
# dp = []
# for i in range(n):
#     dp.append([0]*(i + 1))
# tri = [list(map(int, input().split())) for _ in range(n)]

# dp[0][0] = tri[0][0]
# dp[1][0] = dp[0][0] + tri[1][0]
# dp[1][1] = dp[0][0] + tri[1][1]

# for i in range(2, n):
#     for j in range(1, i + 1):
#         dp[i][j] = tri[i - 1][j-1] + max(tri[i][j - 1], tri[i][j])
# print(max(tri[n - 1]))

# print(tri)


n = int(input())
t = []
for i in range(n):
    t.append(list(map(int, input().split())))
k = 2
for i in range(1, n):
    for j in range(k):
        if j == 0: 
            t[i][j] == t[i][j] + t[i-1][j]
        elif i == j:
            t[i][j] == t[i][j] + t[i - 1][j - 1]
        else:
            t[i][j] == max(t[i - 1][j - 1], t[i - 1][j]) + t[i][j]
    k += 1
print(max(t[n-1]))