# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수
# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다
# import itertools

# def solution(numbers):
#     answer = 0
#     strn = [str(int) for int in numbers]
#     perList = list(itertools.permutations(strn))
#     lists = []
#     for i in perList:
#         lists.append(int(''.join(i)))
#         lists = sorted(lists)
#     answer = str(lists[len(lists) - 1])
#     return answer

# print(solution([3, 30, 34, 5, 9]))
# numbers = [6, 10, 2]
# strn = [str(int) for int in numbers]
# perList = list(itertools.permutations(strn))
# lists = []
# for i in perList:
#     lists.append(int(''.join(i)))
# lists = sorted(lists)

# print(str(lists[len(lists) - 1]))

# return = [[1,6],[8,10],[15,18]]
# intervals = [[1,3],[2,6],[8,10],[15,18]]
# maxNum = max(max(intervals))
# lists = []
# finResult = []
# checkArr = [0 for _ in range(maxNum + 1)]
# for i in range(len(intervals)):
#     checkArr[intervals[i][0]] = 's'
#     checkArr[intervals[i][1]] = 'e'
# i = 0
# while i <= maxNum:
#     y = False
#     if checkArr[i] == 's':
#         lists.append(i)
#         for j in range(i + 1, len(checkArr)):
#             if y:
#                 break
#             if j + 1 == maxNum:
#                 lists.append(j + 1)
#                 finResult.append(lists)
#                 y = True
#                 break
#             elif checkArr[j] == 'e':
#                 for a in range(j + 1, len(checkArr)):
#                     if y:
#                         break
#                     if checkArr[a] == 'e':
#                         break
#                     elif checkArr[a] == 0:
#                         pass
#                     elif checkArr[a] == 's':
#                         lists.append(j)
#                         finResult.append(lists)
#                         i = j + 1
#                         lists = []
#                         y = True
#                         break
#     i += 1
# print(finResult)

# def solution(intervals):
#     maxNum = max(max(intervals))
#     lists = []
#     finResult = []
#     checkArr = [0 for _ in range(maxNum + 1)]
#     for i in range(len(intervals)):
#         checkArr[intervals[i][0]] = 's'
#         checkArr[intervals[i][1]] = 'e'
#     i = 0
#     while i <= maxNum:
#         y = False
#         if checkArr[i] == 's':
#             lists.append(i)
#             for j in range(i + 1, len(checkArr)):
#                 if y:
#                     break
#                 if j + 1 == maxNum:
#                     lists.append(j + 1)
#                     finResult.append(lists)
#                     y = True
#                     i = maxNum + 1
#                     break
#                 elif checkArr[j] == 'e':
#                     for a in range(j + 1, len(checkArr)):
#                         if y:
#                             break
#                         if checkArr[a] == 'e':
#                             break
#                         elif checkArr[a] == 0:
#                             pass
#                         elif checkArr[a] == 's':
#                             lists.append(j)
#                             finResult.append(lists)
#                             i = j + 1
#                             lists = []
#                             y = True
#                             break
#         i += 1
#     return finResult
# print(solution([[1,3],[2,6],[8,10],[15,18]]))


# [0, 's', 's', 'e', 0, 0, 'e', 0, 's', 0, 'e', 0, 0, 0, 0, 's', 0, 0, 'e']
# i == 1

# def solution(intervals):
#     res_arr = []
#     for i in sorted(intervals, key=lambda x: x[0]):
#         if res_arr and i[0] <= res_arr[-1][1]:
#             res_arr[-1][1] = max(res_arr[-1][1], i[1])
#         else:
#             res_arr += i,
#     return res_arr
# print(solution([[1, 4], [4, 5]]))
# from collections import deque

# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbcbcac"
# res = []

# s1 = deque(s1)
# s2 = deque(s2)
# s3 = deque(s3)

# for i in range(len(s3)):
#     if len(s1) > 0 and s1[0] == s3[i]:
#         res.append(s1.popleft())
#     elif len(s2) > 0 and s2[0] == s3[i]:
#         res.append(s2.popleft())
#     else:
#         print('s1 = ', s1)
#         print('s2 = ', s2)
#         print(False)
#         break
# print(res)


# def isInterleave(self, s1, s2, s3):

#     if len(s3) != len(s1) + len(s2):
#         return False

#     last = set()  # ((i,j) , (i2,j2))
#     last.add((-1, -1))

#     for i in range(len(s3)):   # cal f(i)
#         tmp = set()
#         for (m, n) in last:  # (i,j)
#             if m+1 < len(s1) and s3[i] == s1[m+1]:
#                 tmp.add((m+1, n))
#             if n+1 < len(s2) and s3[i] == s2[n+1]:
#                 tmp.add((m, n+1))
#         last = tmp
#         if not last:
#             return False

#     return True


# def isInterleave3(self, s1, s2, s3):
#     # 문자열 각각 길이
#     r, c, l= len(s1), len(s2), len(s3)
#     if r+c != l:
#         return False
#     # ㅁㅊ그냥 true false로 만들지 굳이 배열을 만들어서 저장하지 않음ㄷㄷㄷㄷㄷㄷ
#     dp = [True for _ in xrange(c+1)]
#     for j in xrange(1, c+1):
#         dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
#     for i in xrange(1, r+1):
#         dp[0] = (dp[0] and s1[i-1] == s3[i-1])
#         for j in xrange(1, c+1):
#             dp[j] = (dp[j] and s1[i-1] == s3[i-1+j]) or (dp[j-1] and s2[j-1] == s3[i-1+j])
#     return dp[-1]


# 가장 적은 변환 횟수? 설마 이새끼도?
# 역시 bfs였다
# 시작 문자에서 한 글자씩 바꿔서 문자리스트 문자들을 거쳐 cog로
# from collections import deque

# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]

# wordList = set(wordList)
# # 횟수 세야해서 1넣은듯
# queue = deque([[beginWord, 1]])
# while queue:
#     # word = beginWord, length = 1
#     word, length = queue.popleft()
#     # 같으면 답
#     if word == endWord:
#         print(length)
#     # 같지 않으면 글자 수 마다 반복문
#     # 글자 수 마다 알파벳 돌리면서 브루트포스로 wordList에 있는지 확인하고 있으면 remove
#     for i in range(len(word)):
#         for c in 'abcdefghijklmnopqrstuvwxyz':
#             next_word = word[:i] + c + word[i+1:]
#             if next_word in wordList:
#                 wordList.remove(next_word)
#                 queue.append([next_word, length + 1])

from collections import deque

def solution(beginWord, endWord, wordList):
    wordList = set(wordList)
    q = deque([[beginWord, 1]])

    while q:
        word, cnt = q.popleft()
        if word == endWord:
            return cnt
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordList:
                    wordList.remove(next_word)
                    q.append([next_word, cnt + 1])
    return 0

print(solution('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
