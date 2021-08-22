# 리스트가 들어옴
# 리스트의 중간값을 찾음
# 중간값이 타겟값과 같다면 True 리턴
# 그렇지 않다면 타겟값보다 중간값이 큰지 작은지를 파악
# 타겟값 > 중간값 이라면 중간값 + 1의 인덱스부터 끝까지의 값의 중간값을 중간값으로 만든다.
# 타겟값 < 중간값 이라면 처음 값 부터 중간값 - 1의 인덱스를 중간 값으로 만든다.

# def binary_search(data, search):
#     if len(data) == 1 and search == data[0]:
#         return True
#     if len(data) == 1 and search != data[0]:
#         return False
#     if len(data) == 0:
#         return False

#     medium = len(data) // 2
#     if search == data[medium]:
#         return True
#     else:
#         if search > data[medium]:
#             return binary_search(data[medium:], search)
#         else:
#             return binary_search(data[:medium], search)

# import random
# data_list = random.sample(range(100), 10)
# binary_search(data_list, 7)


# def binary(matrix, target):
#     if target in matrix[0] and len(matrix) == 1:
#         return True
#     if target not in matrix[0] and len(matrix) == 1:
#         return False
#     if len(matrix) == 0:
#         return False
#     mid = len(matrix) // 2
#     if target in matrix[mid]:
#         return True
#     else:
#         if target < matrix[mid][0]:
#             return binary(matrix[:mid], target)
#         elif target > matrix[mid][-1]:
#             return binary(matrix[mid:], target)


# matrix = [
#      [1, 3, 5, 7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]

# target = 13

# print(binary(matrix, target))

# 두 문자열 A와 B가 있을 때, 두 문자열의 '최대공약문자열' C를 아래와 같이 정의하자.

# 문자열 C를 반복하여 문자열 A와 B를 생성할 수 있다.
# 가능한 C 중에 가장 긴 문자열을 C로 한다.
# 위 조건을 만족하는 C가 없으면 빈 문자열을 C로 한다.
# 이 때, 문자열 A와 B를 입력받아 C를 출력하는 프로그램을 작성하시오.

# A = 'ababcde'
# B = 'ababcde'
# 출력: 'ababcde'

# A = 'ababababab'
# B = 'abab'
# 출력: 'ab'
# import sys
# sys.setrecursionlimit(1000)

# A = 'abcabc'
# B = 'abcabc'
# # i = len(a)


# def calStr(a, b):
#     while len(b) > 0:
#         c = ''
#         i = len(a)
#         while i != 0:
#             if b * i == a:
#                 c = b
#                 return c
#             i -= 1
#         b = b[:-1]
#     return c

# def gcdString(a, b):
#     if len(a) > len(b):
#         return print(calStr(a, b))
#     elif len(a) < len(b):
#         return print(calStr(b, a))
#     else:
#         if a == b:
#             c = a
#         return print(c)
# gcdString(A, B)
# if len(A) > len(B):
#     print(calStr(A, B))
# elif len(A) < len(B):
#     print(calStr(B, A))
# else:
#     if A == B:
#         c = A
#     print(c)

# def gcdString(A, B):
#     pass


# ======================================================================

# 1번 노드에서 가장 간선 개수가 많은 노드의 개수. 가장 멀리 떨어진 노드의 개수 == 깊은?
# from collections import deque

# n = 6
# m = 7
# vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# matrix = [[0] * (n + 1) for _ in range(n + 1)]
# for i in range(m):
#     a, b = vertex[i][0], vertex[i][1]
#     matrix[a][b] = matrix[b][a] = 1
# result = 1

# visited = [True] + [False] * n


# def bfs(v):
#     global result
#     queue = deque
#     queue.append(v)
#     # visited[v] = True
#     for i in range(1, n + 1):
#         if visited[i] == False and matrix[v][i] == 1:
#             result += 1
#     return result

# ====================================================
# https://moseory20.tistory.com/35


# from collections import deque

# def solution(n, vertex):
#     ans = 0
#     route = [0] * (n + 1)
#     vertex.sort()
#     queue = deque()
#     graph = [[] for i in range(n + 1)]

#     for e in vertex:
#         graph[e[0]].append(e[1])
#         graph[e[1]].append(e[0])
#     queue.append(1)
#     route[1] = 1

#     while queue:
#         now = queue.popleft()
#         for g in graph[now]:
#             if route[g] == 0:
#                 queue.append(g)
#                 route[g] = route[now] + 1

#     max_vertex = max(route)
#     for r in route:
#         if r == max_vertex:
#             ans += 1
#     return ans
# solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])

# print(dfs(1))
# def quicksort(data_list):
#     if len(data_list) <= 1:
#         return data_list
#     pivot = data_list[0]

#     left = [item for item in data_list[1:] if pivot > item]
#     right = [item for item in data_list[1:] if pivot <= item]

#     return quicksort(left) + [pivot] + quicksort(right)

# data_list = [50, 90, 1, 14, 8, 21, 65]
# print(quicksort(data_list))


# ==============================================================


# if(matrix == null | | matrix.length == 0 | | matrix[0].length == 0) {
#     return false
# }
# int m = matrix.length
# int n = matrix[0].length

# int start = 0
# int end = m*n-1

# while(start <= end) {
#     int mid = (start+end)/2
#     int midX = mid/n
#     int midY = mid % n
#     if(matrix[midX][midY] == target) {
#         return true
#     }
#     if(matrix[midX][midY] < target) {
#         start = mid + 1
#     } else {
#         end = mid - 1
#     }
# }
# return false

# matrix = [
#     [1, 3, 5, 7],
#     [10, 11, 16, 20],
#     [23, 30, 34, 50]
# ]

# target = 3


# def searchMatrix(matrix, target):
#     if len(matrix) == 0 or len(matrix[0]) == 0 or matrix == None:
#         return False
#     m = len(matrix)
#     n = len(matrix[0])
#     start = 0
#     end = m * n - 1
#     while start <= end:
#         mid = (start+end)//2
#         midX = mid//n
#         midY = mid % n
#         if matrix[midX][midY] == target:
#             return True
#         if matrix[midX][midY] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return False
# print(searchMatrix(matrix, target))

# # 프린트를 함수 내 에서 하는 경우
# def test1(a):
#     return print(a)

# test1('test1')

# # 프린트를 채점하는 측에서 하는 경우
# def test2(a):
#     return a

# print(test2('test2'))

# # 어느쪽에서도 프린트를 쓰지 않는 경우. 답이 눈에 보이지 않는다
# def test3(a):
#     return a

# test3('test3')

#=======================================================
# 마을에 1부터 N의 고유 번호를 가진 사람들이 있다. 소문으로는 마을 사람 중에 마을 판사가 있다고 한다. 마을 판사가 실제로 존재한다면,

# 마을 판사는 아무도 믿지 않는다.
# 다른 모든 사람들은 마을 판사를 믿는다.
# 마을 판사가 있다면 오직 한명 뿐이다.
# 리스트 trust가 주어졌을 때, trust[i] = [a, b]는 고유 번호가 a인 사람이 고유 번호가 b인 사람을 믿는다는 것을 의미한다고 한다.

# 마을 판사가 존재한다면 마을 판사의 고유 번호를, 존재하지 않는다면 -1을 출력하는 프로그램을 작성하시오.

# (단, a가 b를 믿고 b가 c를 믿는다고 할 때, a가 c를 믿는다는 의미는 아니다.)
