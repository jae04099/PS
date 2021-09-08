# 1
# 문자열이 뒤에서부터 읽어도 원래 문자열과 같다면 빈 문자열 출력
# 그렇지 않다면 문자열을 반으로 나누어 앞 단어를 펠린드롬으로.

# def solution(s):
#     if list(s) == list(reversed(s)):
#         return ''
#     else:
#         half_string = list(s)[:(len(s) // 2)]
#         result = half_string + list(reversed(half_string))
#         return ''.join(result)


# print(solution('wabe'))


# =========================================================
# 2
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return

# def solution(participant, completion):
#     lose = []
#     for i in range(len(participant)):
#         if participant[i] in completion:
#             completion.remove(participant[i])
#         else:
#             lose.append(participant[i])
#     return lose


# part = ["leo", "leo", "kiki", "eden"]
# comp = ["leo", "eden", "kiki"]

# part = ["marina", "josipa", "nikola", "vinko", "filipa"]
# comp = ["josipa", "filipa", "marina", "nikola"]

# part = ["mislav", "stanko", "mislav", "ana"]
# comp = ["stanko", "ana", "mislav"]

# print(solution(part, comp))
# return "leo"

# ===========================================================
# 3
# def calculator(array, i, j, k):
#     result = sorted(array[i - 1:j])[k - 1]
#     return result

# def solution(array, commands):
#     res = []
#     for i in range(len(commands)):
#         res.append(calculator(array, commands[i][0], commands[i][1], commands[i][2]))
#     return res

# array = [1, 5, 2, 6, 3, 7, 4]
# # [[i, j, k], [i, j, k], [i, j, k]]
# commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# print(solution(array, commands))
# return = [5, 6, 3]

# ==================================================================
# 4
# 5
# 거르는 단계가 있을 것 같음
# 1. 글자 수가 맞는지
# 2. ?가 나올 때 까지의 글자가 맞는지
# 3. 혹은 ?가 끝나고 마지막 글자까지의 글자가 맞는지
# 4. 그래서 각각 맞는 단어들 갯수 result에 append
# def solution(words, queries):
#     for i in range(len(queries)):
#         for j in range(len(words)):
#             if len(queries[i]) == len(words[j]):
#                 if queries[i][0] == '?':


#     res = []
#     return res

# queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
# words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
# print(solution(words, queries))

# list_q = list(sam_q)
# list_w = list(sam_w)
# n = 0
# if len(list_q) == len(list_w):
#     if list_q[-1] == '?':
#         while list_q[n] != '?':
#             if list_q[n] != list_w[n]:
#                 print('물음표가 뒤에부터 시작하지만 매치되지 않습니다.')
#                 break
#             n += 1
#         print('물음표는 뒤에부터 시작하며 매치됩니다.')
#     elif list_q[0] == '?':
#         n = len(sam_q) - 1
#         while list_q[n] != '?':
#             if list_q[n] != list_w[n]:
#                 print('물음표가 앞에부터 시작하지만 매치되지 않습니다.')
#                 break
#             n -= 1
#         print('물음표가 앞에서부터 시작되며 매치됩니다.')
# else:
#     print('서로 자릿수조차 안맞습니다.')

# sam_q = "??odo"
# sam_w = "front"

# def sample_converter(words, queries):
#     list_w = list(words)
#     list_q = list(queries)
#     n = 0
#     if len(list_q) == len(list_w):
#         if list_q[-1] == '?':
#             while list_q[n] != '?':
#                 if list_q[n] != list_w[n]:
#                     return 0
#                 n += 1
#             return 1
#         elif list_q[0] == '?':
#             n = len(list_q) - 1
#             while list_q[n] != '?':
#                 if list_q[n] != list_w[n]:
#                     return 0
#                 n -= 1
#             return 1
#     else:
#         return 0

# def solution(words, queries):
#     res = [0] * len(queries)
#     for i in range(len(queries)):
#         for j in range(len(words)):
#             res[i] += sample_converter(words[j], queries[i])
#     return res

# print(solution(words, queries))

# =====================================================
# 6
# 7

# bfs같음
# 이 게임은 브라운이 코니를 잡거나, 코니가 너무 멀리 달아나면 끝난다. 게임이 끝나는데 걸리는 최소 시간
# lists = [1, '22', 1.222]
# print(lists)

# lists = [1, 1, 1, 2, 4, 2]
# result = []
# for i in lists:
#     if i not in result:
#         result.append(i)
# return result

# def prob20(a:list[int]):
#     if len(a) == 1:
#         return a[0]
#     return a[0] + prob20(a[1:])
# print(prob20([1, 2, 3, 4]))

# # def prob19(x:list[int]):
# #     result = []
# #     for i in x:
# #         if i not in result:
# #             result.append(i)
# #     return result
# # print(prob19([1, 1, 2, 3, 4]))

# for row in range(m):
#     for col in range(n):
#         if(col == 0)

# =================================
# 10

# 정렬시키고 종류가 뭐뭐 있는지 배열 따로 만들기.
# 전체 다 나오면 스탑.

# res = [3, 7]

# res = []
# #["XYZ"]
# lists = list(set(gems))
# for i in range(len(gems)):
#     temp_result = [0] * 2
#     temp_lists = copy.deepcopy(lists)
#     temp_result[0] = i + 1
#     if gems[i] in temp_lists:
#         temp_lists.remove(gems[i])
#         if len(temp_lists) == 0:
#             temp_result[1] == i + 1
#             break
#     for j in range(i, len(gems)):
#         if gems[j] in temp_lists:
#             temp_lists.remove(gems[j])
#             if len(temp_lists) == 0:
#                 temp_result[1] = j + 1
#                 res.append(temp_result)
#                 break
#         else:
#             continue
# print(res)
# import copy

# def short_len(gems):
#     res = []
#     lists = list(set(gems))
#     for i in range(len(gems)):
#         temp_result = [0] * 2
#         temp_lists = copy.deepcopy(lists)
#         temp_result[0] = i + 1
#         if gems[i] in temp_lists:
#             temp_lists.remove(gems[i])
#             if len(temp_lists) == 0:
#                 temp_result[1] = i + 1
#                 res.append(temp_result)
#                 return res
#         for j in range(i, len(gems)):
#             if gems[j] in temp_lists:
#                 temp_lists.remove(gems[j])
#                 if len(temp_lists) == 0:
#                     temp_result[1] = j + 1
#                     res.append(temp_result)
#             else:
#                 continue
#     return res

# def solution(gems):
#     res = short_len(gems)
#     fin_res = res[0]
#     if len(res) == 1:
#         return fin_res
#     for i in range(1, len(res)):
#         if fin_res[1] - fin_res[0] > res[i][1] - res[i][0]:
#             fin_res = res[i]
#     return fin_res

# gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# print(solution(gems))

# gems = ["AA", "AB", "AC", "AA", "AC"]
# print(solution(gems))

# gems = ["XYZ", "XYZ", "XYZ"]
# print(solution(gems))

# gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
# print(solution(gems))

# def solution(participant, completion):
#     participant.sort()
#     completion.sort()

#     for p, c in zip(participant, completion):
#         if p != c :
#             return p
#     return participant[-1]

# def solution(N, duration, cost):
#     dp = [0]*(N+1)

#     def dynamic_programming():
#         max_val = 0
#         for i in range(N-1, -1, -1):
#             if i + duration[i] > N:
#                 dp[i] = dp[i+1]
#             else:
#                 dp[i] = max(dp[i+1], cost[i] + dp[i + duration[i]])
#         max_val = max(dp)
#         return max_val

#     result = dynamic_programming()
#     return result
# N = 10
# duration = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
# cost = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50]
# print(solution(N, duration, cost))
# https://minhyeok-rithm.tistory.com/entry/%EB%A9%94%EB%89%B4-%EB%A6%AC%EB%89%B4%EC%96%BC

# from collections import deque

# def solution(C, B):
#     res = 0
#     visit = [[0]*2 for _ in range(200001)]
#     q = deque()
#     q.append((B, 0))
#     while 1:
#         C += res
#         if C > 200000 or C < 0:
#             return -1
#         if visit[C][res % 2]:
#             return res
#         for _ in range(0, len(q)):
#             current = q.popleft()
#             currentPosition = current[0]
#             newTime = (current[1]+1) % 2
#             newPosition = currentPosition - 1
#             if newPosition >= 0 and not visit[newPosition][newTime]:
#                 visit[newPosition][newTime] = True
#                 q.append((newPosition, newTime))
#             newPosition = currentPosition + 1
#             if newPosition < 200001 and not visit[newPosition][newTime]:
#                 visit[newPosition][newTime] = True
#                 q.append((newPosition, newTime))
#             newPosition = currentPosition * 2
#             if newPosition < 200001 and not visit[newPosition][newTime]:
#                 visit[newPosition][newTime] = True
#                 q.append((newPosition, newTime))
#         res += 1
# print(solution(11, 2))

# N = 6
# K = 3
# L = 3
# apples = [(3, 4), (2, 5), (5, 3)]
# moves = [(3, 'D'), (15, 'L'), (17, 'D')]

# matrix = [[0] * N for _ in range(N)]

# for i in apples:
#     matrix[i[0]-1][i[1]-1] = 2

# x,y = 0, 0
# s_dir = 0

# tail = []
# tail.append([0,0])

# dx = [0,1,0,-1]
# dy = [1,0,-1,0]

# matrix[0][0] = 1
# res = 0

# while True:
#     if len(moves) != 0:
#         if res == int(moves[0][0]):
#             D = moves.pop(0)[1]
#             if D == "D":
#                 s_dir = ( s_dir + 1 ) % 4
#             else:
#                 s_dir = (s_dir - 1) % 4

#     nx = x + dx[s_dir]
#     ny = y + dy[s_dir]

#     if nx < 0 or ny < 0 or nx >= N or ny >= N or matrix[nx][ny] == 1:
#         res += 1
#         break
#     else:
#         if matrix[nx][ny] == 2:
#             matrix[nx][ny] = 1
#             tail.append([nx, ny])
#         else:
#             t_x, t_y = tail.pop(0)
#             matrix[t_x][t_y] = 0
#             matrix[nx][ny] = 1
#             tail.append([nx,ny])
#     x,y = nx, ny
#     res += 1
# return res

# print(res)

# def solution(N, K, L, apples, moves):
#     matrix = [[0] * N for _ in range(N)]

#     for i in apples:
#         matrix[i[0]-1][i[1]-1] = 2

#     x,y = 0, 0
#     s_dir = 0

#     tail = []
#     tail.append([0,0])

#     dx = [0,1,0,-1]
#     dy = [1,0,-1,0]

#     matrix[0][0] = 1
#     res = 0

#     while True:
#         if len(moves) != 0:
#             if res == int(moves[0][0]):
#                 D = moves.pop(0)[1]
#                 if D == "D":
#                     s_dir = ( s_dir + 1 ) % 4
#                 else:
#                     s_dir = (s_dir - 1) % 4

#         nx = x + dx[s_dir]
#         ny = y + dy[s_dir]

#         if nx < 0 or ny < 0 or nx >= N or ny >= N or matrix[nx][ny] == 1:
#             res += 1
#             break
#         else:
#             if matrix[nx][ny] == 2:
#                 matrix[nx][ny] = 1
#                 tail.append([nx, ny])
#             else:
#                 t_x, t_y = tail.pop(0)
#                 matrix[t_x][t_y] = 0
#                 matrix[nx][ny] = 1
#                 tail.append([nx,ny])
#         x,y = nx, ny
#         res += 1
#     return res
# print(solution(10, 5, 4, [(1, 5), (1, 3), (1, 2), (1, 6), (1, 7)], [(8, 'D'), (10, 'D'), (11, 'D'), (13, 'L')]))

# visit = [0 for i in range(3)]
# formula = ["+", "-", "*"]
# priority = []
 
# def calculator(a, b, p):
#     if p == "+":
#         return a + b
#     elif p == "-":
#         return a - b
#     else:
#         return a * b
 
 
# def dfs(idx, temp):
#     global visit, priority
 
#     if idx == 3:
#         priority.append(temp[:])
#         return
 
#     for i in range(3):
#         if visit[i] == 1:
#             continue
#         visit[i] = 1
#         temp.append(formula[i])
#         dfs(idx + 1, temp)
#         temp.pop()
#         visit[i] = 0
 
 
# def solution(exp):
#     res = 0
#     formula_list = []
#     num_list = []
#     slice_idx = 0
 
#     for i in range(len(exp)):
#         if exp[i] in formula:
#             formula_list.append(exp[i])
#             num_list.append(int(exp[slice_idx:i]))
#             slice_idx = i + 1
 
#     num_list.append(int(exp[slice_idx:]))

#     dfs(0, [])
   
#     for prior in priority:
#         temp_formula = formula_list[:]
#         temp_num = num_list[:]
#         for p in prior:
#             i = 0
#             while (i < len(temp_formula)):
#                 if p == temp_formula[i]:
#                     num1 = temp_num[i]
#                     num2 = temp_num.pop(i + 1)
#                     temp_num[i] = calculator(num1, num2, p)
#                     temp_formula.pop(i)
#                     i -= 1
#                 i += 1
#         if abs(temp_num[0]) > res:
#             res = abs(temp_num[0])
 
#     return res
# print(solution('100-200*300-500+20'))

from collections import defaultdict 

def solution(gems):
    gem_list = defaultdict(int)
    gem_list[gems[0]] = 1
    N = len(set(gems))

    span = len(gems) + 1
    left, right = 0, 0

    while True:
        if left < 0 or right > len(gems)-1:
            break

        if len(gem_list) == N:
            if right - left + 1 < span:
                answer = [left+1, right+1]
                span = right - left + 1
            left += 1 
            gem_list[gems[left-1]] -= 1 
            if gem_list[gems[left-1]] == 0:
                gem_list.pop(gems[left-1])

        else:
            right += 1 
            if right < len(gems):
                gem_list[gems[right]] += 1 

    return answer

print(solution( ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))