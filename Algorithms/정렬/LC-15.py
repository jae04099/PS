# import itertools
# numlist = []
# result = []

# if len(nums) < 3:
#     print(result)
# numlist = list(itertools.combinations(nums, 3))
# for i in numlist:
#     if sum(i) == 0:
#         result.append(i)
# for i in range(len(result)):
#     result[i] = sorted(result[i])
# result = list(set([tuple(t) for t in result]))
# for i in range(len(result)):
#     result[i] = list(result[i])
# print(result)
# print(list(itertools.combinations(nums, 3)))

# items = [[1, 2], [2, 1], [1, 3]]
# items = list(set(map(tuple, items)))
# print(items)

nums = [-1, 0, 1, 2, -1, -4]

