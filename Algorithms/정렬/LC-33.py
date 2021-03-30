nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

if target not in nums:
    print(-1)
for i in range(len(nums)):
    if nums[i] == target:
        print(i)