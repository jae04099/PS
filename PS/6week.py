
# import itertools

# def solution(n, k):
#     lists = [i for i in range(1, n + 1)]
#     permu = list(itertools.permutations(lists))
#     return list(permu[k - 1])

# print(solution(4, 9))


# for i in range(1, 8):
#     if i == 1:
#         if n == num:
#             print(1)
#             break
#     elif i == 2:
#         if n + n == num or n / n == num or n * n == num or int('n' + 'n') == num or n - n == num:
#             print(2)
#             break
#     else:


# def solution(N, number):
#     # ex) 5, 12
#     # [{5}, {55}, {555}, {5555}, {55555}, {555555}, {5555555}, {55555555}]
#     dp = [set([N*int('1'*i)]) for i in range(1, 9)]
# # {k번 집합} = {k-i번 집합} (사칙연산) {i번 집합}
#     for i in range(8):
#         for j in range(i):
#             for a in dp[j]:
#                 for b in dp[i-j-1]:
#                     dp[i].add(a + b)
#                     dp[i].add(a - b)
#                     dp[i].add(a * b)
#                     if b != 0:
#                         dp[i].add(a // b)

#         print(dp)
#         if number in dp[i]:
#             return i + 1
#     return -1

# print(solution(5, 12))



# n개의 정수로 이루어진 리스트 nums와 정수 target이 주어졌을 때, nums에 있는 정수 4개를 합하여 target을 만들 수 있는 모든 조합을 구하시오. 단, 정답에는 동일한 정수 조합이 여러개 포함되어서는 안된다.

# print = [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]

# from itertools import combinations

# def solution(nums, target):
#     res = []
#     nums = sorted(nums)
#     lists = list(combinations(nums, 4))
#     for i in lists:
#         if sum(i) == target:
#             res.append(list(i))
#     return res

# print(solution([1, 0, -1, 0, -2, 2], 0))


# x = [-1, -1, -1, -1, 0, 1, 20, 19, 17]
# res = 6

# logn인 탐색은 바이너리트리밖에 없는데 바이너리는 오름차순 혹 내림차순임.
# 근데 자세히 보면 특정 숫자 기준으로 왼쪽 오른쪽이 순차인듯?
# 그래서 반드시 ~ 조건이 붙은듯

# 아마 가장 큰 수를 기준으로 리스트를 이분할 하고, 그 수가 피크가 아니면 왼쪽 오른쪽 따지나? tlqkf

# pick = x.index(max(x))
# left, right = x[:pick - 1], x[pick - 1:]
# if right[0] < right[1] and right[2] < right[1]:
#     print(right[1])

# N, M, V = 4, 5, 1
# edges = [[1, 2], [1, 3], [1,4], [2, 3], [3, 4]]
# # 1 2 3 4

# def solution(N, M, V, edges):
#     matrix = [[0] * (N + 1) for _ in range(N + 1)]
#     visited = [0] * (N + 1)
#     for i in range(M):
#         a, b = edges[i][0], edges[i][1]
#         matrix[a][b] = matrix[b][a] = 1

#     def dfs(start):
#         visited[start] = 1
#         print(start, end=' ')
#         for i in range(1, N + 1):
#             if visited[i] == 0 and matrix[start][i] == 1:
#                 dfs(i)
#     dfs(V)

# solution(N, M, V, edges)

x = [-1, -1, -1, -1, 0, 1, 20, 19, 17]
res = 20

def solution(x):
    left, right = 0, len(x) - 1
    while left < right:
        mid = left + (right - left) // 2
        if x[mid] < x[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return x[left]

print(solution(x))