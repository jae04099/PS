# import sys
# n = int(sys.stdin.readline())
# list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# print(list)
# list = sorted(list, key=lambda x : (x[1], x[0]))
# print(list)
# count = 1
# prev = list[0][1]
# print(prev)

# for i in list[1:]:
#     if prev <= i[0]:
#         prev = i[1]
#         count += 1
# print(count)

import sys
n = int(sys.stdin.readline())
list = [list(map(int, sys.stdin.readline())) for _ in range(n)]

list = sorted(list, key=lambda x:(x[1], x[0]))
count = 1
prev = list[0][1]

for i in list[1:]:
    if prev <= i[0]:
        prev = i[1]
        count += 1
print(count)