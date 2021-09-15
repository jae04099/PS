citations = [0, 0, 0, 0, 0, 0]
# 논문 n편 중 h번 이상 인용된 논문이 h편 이상이고 나머지가 h번 이하 인용
# h의 최댓값 구하기

# [20, 19, 18, 1]
# [22, 42]
# [5, 5, 5, 5]

# [0, 1, 3, 5, 6]
# 0회 이상: 5개
# 1회 이상: 4개
# 3회 이상: 3개
# ------------
# 5회 이상: 2개
# 6회 이상: 1개

# [10, 50, 100]
def solution(citations):
    citations.sort()
    if max(citations) == 0:
        return 0
    for i in range(len(citations)):
        if citations[i] <= len(citations) - i:
            continue
        elif citations[i] > len(citations) - i:
            return len(citations) - i
print(solution(citations))