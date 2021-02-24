# n = int(input())
# d = [[0] * 10 for _ in range(1001)]


# for i in range(10):
#     d[1][i] = 1

# for i in range(2, 1001):
#     for j in range(10):
#         for k in range(j + 1):
#             d[i][j] += s[i - 1][k]
# print(sum(d[n]) % 10007)

# import sys 
# N = int(sys.stdin.readline()) 
# nums = [1] * 10 
# mod = 10007 
# for _ in range(N-1): 
#     for i in range(1, 10): 
#         nums[i] = (nums[i] + nums[i-1]) % mod 
# sys.stdout.write(str(sum(nums) % mod))

# n = int(input())
# dp = [[1]*10]
# dp.append(list([0] * 10 for _ in range(n)))

# for i in range(1, n + 1):
#     for j in range(10):
#         for k in range(j + 1):
#             dp[i][j] += dp[i-1][k]

n = int(input())
dp = [[0] * 10 for _ in range(n + 1)]

for i in range(1 , 10):
    dp[1][i] = 1