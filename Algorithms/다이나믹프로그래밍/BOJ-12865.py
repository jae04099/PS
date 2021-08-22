# # n = 물품의 수 / k = 가방이 버틸 수 있는 무게 / weight = 물건의 무게 / value = 물건의 가치

# # 물품의 수, 가방이 버틸 수 있는 무게
# n, k = map(int, input().split())

# # 가방이 버틸 수 있는 무게들을  1부터 행, 물품의 수 만큼 열
# dp = [[0] * (k + 1) for _ in range(n + 1)]

# # 1 번째 물품 부터
# for i in range(1, n + 1):
#     #  정보 기입
#     weight, value = map(int, input.split())
#     # 무게를 1부터 비교
#     for j in range(1, k + 1):
#         # 만약 가방이 버틸 수 있는 무게 j보다 물건 무게가 무거우면
#         if j < weight:
#             # 못 넣으니까 이전 물건에서의 값 받아옴
#             dp[i][j] = dp[i - 1][j]
#         # 그렇지 않다면
#         else:
#             # 현재 값은 이전 물건에서의 결과값과 지금 보는 물건 가치와 전체 무게에서 이 무게를 뺸 값의 결과값을 더한것 중 큰 값이 된다.
#             dp[i][j] = max(dp[i - 1][j],  dp[i - 1][j - weight] + value)
# print(dp[n][k])


n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    w, v = map(int, input().split())
    for j in range(1, k + 1):
        if w > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
print(dp[n][k])