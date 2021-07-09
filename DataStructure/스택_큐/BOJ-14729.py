import sys
input = sys.stdin.readline
n = int(input())
lim = 7
lists = []
for i in range(n):
    lists.append(float(input()))
sorList = sorted(lists)
for i in range(lim):
    print("{:.3f}".format(sorList[i]))
# for i in range(7):

# print(lists)

# 1, 2, 4, 5, 7, 8
# 1, 2, 3, 4, 5, 6

# 과제1번 코드란
# leng = 8
# star = '*'
# result = ''
# for i in range(leng):
#   result += star
#   if (i + 1) % 3 == 0:
#     continue
#   print(result)

# 과제 2
# a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# a = list(map(lambda x : str(int(x) + 1), a))
# print(a)

# a = ['base ball', 'basket ball', 'soccer', 'base ball', 'soccer', 'soccer', 'basket ball', 'base ball', 'basket ball', 'soccer', 'basket ball', 'basket ball', 'base ball', 'soccer', 'soccer', 'basket ball', 'basket ball', 'base ball', 'base ball']

# cat = list(set(a))
# cnt = 0
# for i in range(len(cat)):
#     if cat[i] in a:
#         cnt = a.count(cat[i])
#         print(cat[i], cnt)
#         cnt = 0


# 과제 4번 코드란
# a = 0
# n = 11

# print(a, end=' ')
# for i in range(n):
#   if a == 0:
#     a += 1
#     print(a, end=' ')
#   elif a >= 256:
#     print(256, end=' ')
#   else:
#     a *= 2
#     print(a, end=' ')
