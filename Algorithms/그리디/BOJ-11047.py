# n = 10
# k = 4200
# coins = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]

n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
result = 0

coins = coins[::-1]
for i in range(n):
    if k // coins[i] > 0:
        result += k // coins[i]
        k = k % coins[i]
print(result)