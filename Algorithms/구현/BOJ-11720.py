n = int(input())
nums = list(map(int, input()))
result = 0

for i in range(n):
    result += nums[i]

print(result)