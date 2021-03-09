one = [1, 2, 3, 4, 5]
two = [2, 1, 2, 3, 2, 4, 2, 5]
three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
result = [0, 0, 0]
finresult = []

for i in range(len(answers)):
    if one[i % 5] == answers[i]:
        result[0] += 1
    if two[i % 8] == answers[i]:
        result[1] += 1
    if three[i % 10] == answers[i]:
        result[2] += 1
maxnum = max(result)
for i in range(len(result)):
    if result[i] == maxnum:
        finresult.append(i + 1)
print(finresult)
        