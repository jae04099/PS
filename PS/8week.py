# 분열하여 두 개체로 완전히 나뉘는데 1분
# 분열한 아메바 중 하나는 곧바로 분열 시작, 다른 하나는 1분간 휴식 후 분열 시작
# 분열하면 기존 개체는 사라지고 새 두 개체가 생긴것으로 봄
# 분열되는 중에는 기존 개체가 남아있고 새로운 개체가 생기지 않은것으로 봄.

# 아메바 한 개체를 분열 시작 후 n분 후 까지 만들어진 모든 아메바 개체에 새로운 이름
# 준비해야하는 아메바의 이름 갯수

# dp인듯
# def dp2maker(n):
#     dp2 = [0] * (n + 1)
#     dp2[0], dp2[1], dp2[2] = 1, 2, 2
#     for i in range(3, n + 1):
#         dp2[i] = dp2[i-1] + dp2[i-2]
#     return dp2[n]

# def dp(n):
#     dp = [0] * (n + 3)
#     dp[0], dp[1], dp[2] = 1, 2, 5
#     if n < 3:
#         return dp[n]
#     for i in range(3, n + 1):
#         dp[i] = dp[i-1] + dp2maker(i)
#     return dp[n]

# def solution(N):
#     return dp(N)

# print(solution(4))

#  i번째 자동 튀김기는 치킨을 한 번 튀기는 데에 fry[i] 만큼의 시간
# 튀김이 한번 끝나면 clean[i] 만큼의 시간동안 자동 세척
# 철수가 C 번 치킨을 튀겨내려고 할 때, 최소한 몇 시간 동안 자동 튀김기를 가동

# 제약 사항

# 0 < N <= 100000
# fry[i]는 0 < fry[i] <= 100를 만족하는 정수
# clean[i]는 0 < clean[i] <= 100를 만족하는 정수
# 0 < C <= 100000

n = 4 # 튀김기 개수
fry = [2, 2, 1, 3]  # 각 튀김기가 튀기는 시간
clean = [2, 4, 3, 2]    # 튀기고 세척하는 시간
fry_w_clean = [0] * (n)
for i in range(n):
    fry_w_clean[i] = fry[i] + clean[i]
print(fry_w_clean)
res = 0
c = 2   # 치킨 튀기려는 횟수
# return = 2
dp = [0] * (c + 1)
# for i in range(n):

# if n >= c:
#     r



# =============================================

# 숫자 n진수로 셈
# 9보다 큰 자리 표현: 10 ~ 35: a ~ z(소문자)
# 36 ~ 61: A ~ Z (대문자)

# 2 < N <= 62, start < end이며, counts의 길이는 (end - start + 1)
# 잘못 센 숫자 갯수 반환
# 14진수
# 0 1 2 3 4 5 6 7 8 9 a b c d e
# 9 a c d e가 아니고 9 a b c d라서 3개 잘못됐으니 3
# n진수 배열 만들기
# lists = []
# cor_lists = []
# N = 62
# start = 'Z'
# end ='12'
# counts = ['Z', '10', '11', '12']
# fin_res = 0

# for i in range(N):
#     if i < 10:
#         lists.append(str(i))
#     elif 10 <= i <= 35:
#         lists.append(chr(i + 87))
#     else:
#         lists.append(chr(i + 29))

# def convert_to_ten(a):
#     sample = list(reversed(list(a)))
#     res = int()
#     for i in range(len(sample)):
#         for j in range(len(lists)):
#             if sample[i] == lists[j]:
#                 res += j*(N**i)
#     return res

# def convert_notation(n, base):
#     q, r = divmod(n, base)
#     return convert_notation(q, base) + lists[r] if q else lists[r]

# len_cnt = convert_to_ten(end) - convert_to_ten(start) + 1
# cor_lists = [0] * len_cnt

# cor_lists[0] = start
# for i in range(len_cnt):
#     cor_lists[i] = convert_notation(convert_to_ten(cor_lists[0]) + i, N)

# for i in range(len_cnt):
#     if counts[i] != cor_lists[i]:
#         fin_res += 1
# print(fin_res)

lists = []
cor_lists = []

def convert_to_ten(a, N):
    sample = list(reversed(list(a)))
    res = int()
    for i in range(len(sample)):
        for j in range(len(lists)):
            if sample[i] == lists[j]:
                res += j*(N**i)
    return res

def convert_notation(n, base):
    q, r = divmod(n, base)
    return convert_notation(q, base) + lists[r] if q else lists[r]

def solution(N, start, end, counts):
    answer = 0
    for i in range(N):
        if i < 10:
            lists.append(str(i))
        elif 10 <= i <= 35:
            lists.append(chr(i + 87))
        else:
            lists.append(chr(i + 29))
    len_cnt = convert_to_ten(end, N) - convert_to_ten(start, N) + 1
    cor_lists = [0] * len_cnt
    cor_lists[0] = start
    for i in range(len_cnt):
        cor_lists[i] = convert_notation(convert_to_ten(cor_lists[0], N) + i, N)

    for i in range(len_cnt):
        if counts[i] != cor_lists[i]:
            answer += 1
    return answer
print(solution(62, 'Z',	'12', ['Z', '10', '11', '12']))
# ==================================

# n = int(input())
# t = []
# p = []
# dp = []
# for i in range(n):
#     a, b = map(int, input().split())
#     t.append(a)
#     p.append(b)
#     dp.append(b)
# dp.append(0)
# for i in range(n - 1, -1, -1):
#     if t[i] + i > n:
#         dp[i] = dp[i + 1]
#     else:
#         dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
# print(dp[0])

# def napsek(n, k1, k2)

# def maxWeight(arr, n, w1_r, w2_r, i):
 
#     # Base case
#     if i == n:
#         return 0
#     if dp[i][w1_r][w2_r] != -1:
#         return dp[i][w1_r][w2_r]
 
#     # Variables to store the result of three
#     # parts of recurrence relation
#     fill_w1, fill_w2, fill_none = 0, 0, 0
 
#     if w1_r >= arr[i]:
#         fill_w1 = arr[i] + maxWeight(arr, n, w1_r - arr[i],
#                                              w2_r, i + 1)
 
#     if w2_r >= arr[i]:
#         fill_w2 = arr[i] + maxWeight(arr, n, w1_r,
#                                      w2_r - arr[i], i + 1)
 
#     fill_none = maxWeight(arr, n, w1_r, w2_r, i + 1)
 
#     # Store the state in the 3D array
#     dp[i][w1_r][w2_r] = max(fill_none, max(fill_w1,
#                                            fill_w2))
 
#     return dp[i][w1_r][w2_r]
 
 
# # Driver code
# if __name__ == "__main__":
 
#     # Input array
#     arr = [8, 2, 3]
#     maxN, maxW = 31, 31
     
#     # 3D array to store
#     # states of DP
#     dp = [[[-1] * maxW] * maxW] * maxN
     
#     # Number of elements in the array
#     n = 4
 
#     # Capacity of knapsacks
#     w1, w2 = 3, 8
 
#     # Function to be called
#     print(maxWeight(arr, n, w1, w2, 0))
     