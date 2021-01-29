# import sys
# n = int(sys.stdin.readline())
# lists = list(int(sys.stdin.readline()) for _ in range(n))
# lists.sort(key=lambda x : (x))
# for i in lists:
#     print(i)

import sys
n = int(sys.stdin.readline())
lists = [0] * 10001
for i in range(n):
    lists[int(sys.stdin.readline())] += 1
for i in range(10001):
    if lists[i] != 0:
        for j in range(lists[i]):
            print(i)
