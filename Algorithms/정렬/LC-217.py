nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
result = 0

nums = sorted(nums)
compare = nums[0]
for i in range(1, len(nums)):
    if compare == nums[i]:
        print(True)
        break
    else:
        compare = nums[i]
print(False)