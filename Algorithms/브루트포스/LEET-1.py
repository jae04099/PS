import itertools
nums = [2, 7, 11, 15]
target = 9
result = ()
finresult = []
lists = list(itertools.combinations(nums, 2))

for i in range(len(lists)):
    if sum(lists[i]) == target:
        result = lists[i]
        break
for i in range(len(nums)):
    if nums[i] == result[0]:
        finresult.append(i)
    elif nums[i] == result[1]:
        finresult.append(i)
        break
print(finresult)


for i, num in enumerate(nums):
    n = target - num
    if n not in h