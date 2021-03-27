import math
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_subarray = -math.inf
for i in range(len(nums)):
    cur_subarray = 0
    for j in range(i, len(nums)):
        cur_subarray += nums[j]
        max_subarray = max(max_subarray, cur_subarray)
print(max_subarray)