#n * 2 + m * 1
# 대회 참여하려는 k명은 반드시 인턴쉽
# 인턴쉽 참여하면 대회 참여 못함
# 최대한 많은 팀

n, m, k = map(int, input().split())
result = 0

while n > 2 and m > 1 and n + m > k + 3:
    result += 1
    n -= 2
    m -= 1
print(result)
