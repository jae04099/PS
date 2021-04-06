# import math
# nums = [-1,1,0,-3,3]
# res = [0] * len(nums)
# for i in range(len(nums)):
#     fakenums = nums.copy()
#     del fakenums[i]
#     res[i] = math.prod(fakenums)
# print(res)

# nums = [-1, 1, 0, -3, 3]
# p = 1
# output = []
# for i in range(len(nums)):
#     output.append(p)
#     p = p * nums[i]
# p = 1
# for i in range(n - 1,  -1, -1):
#     output[i] = output[i] * p
#     p = p * nums[i]
# print(output)

nums = [-1, 1, 0, -3, 3]
right, left = [], []
p = 1

for i in range(len(nums)):
    left.append(p)
    p = p * nums[i]
p = 1
for i in range(len(nums) - 1, -1, -1):
    right.append(p)
    p = p * nums[i]
right.reverse()

for i in range(len(nums)):
    right[i] = right[i] * left[i]
print(right)