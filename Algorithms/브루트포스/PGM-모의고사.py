# one = [1, 2, 3, 4, 5]
# two = [2, 1, 2, 3, 2, 4, 2, 5]
# three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
# result = [0, 0, 0]
# finresult = []

# for i in range(len(answers)):
#     if one[i % 5] == answers[i]:
#         result[0] += 1
#     if two[i % 8] == answers[i]:
#         result[1] += 1
#     if three[i % 10] == answers[i]:
#         result[2] += 1
# maxnum = max(result)
# for i in range(len(result)):
#     if result[i] == maxnum:
#         finresult.append(i + 1)
# print(finresult)
        

def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    res = [0, 0, 0]

    fin_res = []
    n = 0
    while n <= len(answers) - 1:
        if answers[n] == first[n % (len(first))]:
            res[0] += 1
        if answers[n] == second[n % (len(second))]:
            res[1] += 1
        if answers[n] == third[n % (len(third))]:
            res[2] += 1
        n += 1


    max_value = max(res)
    for i in range(len(res)):
        if res[i] == max_value:
            fin_res.append(i + 1)
    return fin_res
print(solution([1, 3, 2, 4, 2]))