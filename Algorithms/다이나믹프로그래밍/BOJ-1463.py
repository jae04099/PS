# n = int(input())
# d = [0] * (n + 1)
# for i in range(2, n + 1):
#     d[i] = d[i - 1] + 1
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3] + 1)
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i // 2] + 1)
# print(d[n])

# dp = [0] * 1001
# n = int(input())
# dp[0] = 0
# dp[1] = 1
# dp[2] = 2

# for i in range(3, n + 1):
#     dp[i] = dp[i - 2] + dp[i - 1]
# print(dp[9])


# phone_book = ["119", "97674223", "1195524421"]
# phone_book.sort()
# for i in range(len(phone_book) - 1):
#     if phone_book[i] in phone_book[i + 1]:
#         print(False)
    
