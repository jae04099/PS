# N개의 문자열로 이루어진 List에서 전체 문자열이 앞 n개 문자열이 같다고 할때, 가장 큰 n을 출력하는 알고리즘을 구현하라. (즉, 주어진 모든 문자열의 앞의 몇개의 문자가 일치하는지 출력하라)
# def solution(a):
#     result = 0
#     compChar = 0
#     resultList = []
#     for i in range(1, len(a)):
#         compChar = a[i - 1]
#         j = 0
#         while compChar[j] == a[i][j]:
#             result += 1
#             j += 1
#         resultList.append(result)
#         result = 0
#     return min(resultList)
# # Test code
# print(solution(['abcd', 'abce', 'abchg', 'abcfwqw', 'abcdfg'])) # 3
# print(solution(['abcd', 'gbce', 'abchg', 'abcfwqw', 'abcdfg'])) # 0
# def countUniques(a):
#     result = 1
#     for i in range(1, len(a)):
#         if a[i - 1] != a[i]:
#             result += 1
#     return result
# # Test code
# print(countUniques([-1, 1, 1, 1, 1, 4, 4, 4, 4, 10, 14, 14])) # 5
# print(countUniques([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])) # 2
# print(countUniques([0, 0, 0, 0, 0])) # 1


# 자연수 중, 각 자리수를 제곱한 것을 더하는 과정을 반복했을 때 1으로 끝나는 수를 '행복한 수'라고 한다. '행복한 수'가 아닌 경우 이 과정이 1에 도달하지 못하고 같은 수열이 반복되는 무한 루프에 빠지게 된다. 자연수를 입력받았을 때 '행복한 수'인지 판별하는 알고리즘을 작성하라.

# '행복한 수'를 찾는 과정의 예

#   19가 행복한 수인지 확인하는 과정
#   1^2 + 9^2 = 82
#   8^2 + 2^2 = 68
#   6^2 + 8^2 = 100
#   1^2 + 0^2 + 0^2 = 1 --> True

# def solution(n):
#     res = str(n)
#     try:
#         def happy(n):
#             for i in range(len(str(n))):
#                 n = int(n[i]) * int(n[i])
#             if n == 1:
#                 return True
#             else:
#                 return happy(n)
#         happy(res)
#         print('??')
#     except:
#         return False
# Test code
# def solution(n):
#     res = n
#     def happy(n):
#             for i in range(len(str(n))):
#                 n = int(n[i]) * int(n[i])
#             if n == 1:
#                 return True
#             else:
#                 return happy(n)
#     happy(res)
#     print('??')

# print(solution(19)) # True
# print(solution(61)) # False

# def happy(n):
#     for i in range(len(n)):
#         n += int(res[i]) * int(res[i])
#     return happy(n)

# res = 0
# n = str(19)
# print(n[1])
# res += n[1] * n[1]
# print(res)

# def solution(n):
#     try:
#         def happy(num):
#             res = 0
#             while num//1 != 0:
#                 res += (num%10)**2
#                 num = int(res/10)
#             return (res)
        
#         while True:
#             n = happy(n)
#             if n == 1:
#                 return
#                 break
#     except:
#         return False
    
# def solution(n):
#     lists = [] 
#     while n!= 1 :
#         res = 0
#         string = str(n)
#         for i in string :
#             res += int(i)**2
#         if res in lists :
#             return False
#         lists.append(res)
#         n = res
#     return True

# print(solution(19)) # True
# print(solution(61)) # False

# 방문을 해야 할 큐
# need_visit = []
# 이미 방문 한 큐
# visited = []

# def bfs(graph, start_node):
#     visited = list()
#     need_visit = list()
#     need_visit.append(start_node)
#     while need_visit:
#         node = need_visit.pop()
#         if node not in visited:
#             visited.append(node)
#             need_visit.extend(graph[node])
#     return(visited)

# n, m, v = map(int, input().split())
# lists = [list(map(int, input().split())) for _ in range(m)]

# def bfs(graph, start_node):
#     visited = list()
#     need_visit = list()
#     need_visit.append(start_node)
#     while need_visit:
#         node = need_visit.pop()

print(len('asdf'))