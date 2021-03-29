max_result = 0
nums = [-2]
max_prod, min_prod, ans = nums[0], nums[0], nums[0]
for i in range(1, len(nums)):
    max_prod = max(nums[i], max_prod * nums[i], min_prod*nums[i])
    min_prod = min(nums[i], max_prod*nums[i], min_prod*nums[i])
    # max_prod, min_prod = x, y
    ans = max(max_prod, ans)
print(ans)