import collections, itertools

nums = [6, 10, 2]
numlist = list(map(str, nums))
numlist.sort(key=lambda x: x * 3, reverse=True)
print(str(int(''.join(numlist))))