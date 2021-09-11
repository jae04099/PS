# import sys
# input = sys.stdin.readline

# n = int(input())
# nLists = sorted(list(map(int, input().split())))
# m = int(input())
# mLists = sorted(list(map(int, input().split())))
# count={}

# for i in nLists:
#     try: count[i] += 1
#     except: count[i] = 1

# def binary(i, count, first, last):
#     mid = (first + last) // 2
#     num = 0
#     # if i == count[mid]:

# for i in mLists:
#     first, last = 0, n - 1
#     binary(i, nLists, first, last)


# print(count[3])


# from sys import stdin
# from collections import Counter
# _ = stdin.readline()
# n = stdin.readline().split()
# _ = stdin.readline()
# m = stdin.readline().split()

# c = Counter(n)
# print(c)
# print(' '.join(f'{c[m]}' if i in c else '0' for i in m))

from sys import stdin
from collections import Counter
_ = stdin.readline()
N = stdin.readline().split()
_ = stdin.readline()
M = stdin.readline().split()

C = Counter(N)
print(C)
print(' '.join(f'{C[m]}' if m in C else '0' for m in M))