# import sys
# n, m = map(int, sys.stdin.readline().split())
# lists = list(map(int, sys.stdin.readline().split()))
# start = 1
# end = max(lists)
# while start <= end:
#     mid = (start + end) // 2
#     result = 0
#     for i in lists:
#         if i >= mid:
#             result += i - mid
#     if result >= m:
#         start = mid + 1
#     else:
#         end = mid - 1
# print(end)

import sys
k, n = map(int, sys.stdin.readline().split())
lists = []
for i in range(k):
    lists.append(int(input()))

start = 1
end = max(lists)

while start <= end:
    mid = (start + end) // 2
    result = 0
    for i in lists:
        result += i // mid
    if result >= n :
        start = mid + 1
    else:
        end = mid - 1
print(end)