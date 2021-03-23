prices = [7, 1, 5, 3, 6, 4]
result = 0
buy = prices[0]
max_profit = 0

for i in range(1, len(prices)):
    profit = prices[i] - buy
    if profit > max_profit:
        max_profit = profit
    if buy > prices[i]:
        buy = prices[i]
print(max_profit)

# for i in range(len(prices)):
#     for j in range(i+1, len(prices)):
#         if prices[i] < prices[j]:
#             result = max(result, prices[j] - prices[i])
print(result)