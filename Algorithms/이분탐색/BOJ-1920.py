import sys
input = sys.stdin.readline

# n = int(input())
# nlists = sorted(list(map(int, input().split())))
# m = int(input())
# mlists = sorted(list(map(int, input().split())))

# m의 각 수들이 n에 있는지 

n = 5
nlists = [1, 2, 3, 4, 5]
m = 5
mlists = [1, 3, 5, 7, 9]
def binary(i, start, end):
    if start > end:
        return print(0, end='\n')
    while start <= end:
        mid = (start + end) // 2
        if nlists[mid] == mlists[i]:
            return print(1, end='\n')
        if nlists[mid] < mlists[i]:
            start = mid + 1
        elif nlists[mid] > mlists[i]:
            end = mid - 1
for i in range(m):
    start, end = 0, n - 1
    binary(i, start, end)
# def binary(i, nlists, start, end):
#     if start > end:
#         return 0
#     mid = (start + end) // 2
#     if i == nlists[mid]:
#         return 1
#     elif i < nlists[mid]:
#         return binary(i, nlists, start, mid - 1)
#     else:
#         return binary(i, nlists, mid + 1, end)

# for i in mlists:
#     start = 0
#     end = n - 1
#     print(binary(i, nlists, start, end))

#=============================================

# n = 5
# nlists = [1, 2, 3, 4, 5]
# m = 5
# mlists = [1, 3, 5, 7, 9]

