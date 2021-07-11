from collections import deque
n = int(input())
stack = [list(input()) for i in range(n)]
cnt = 0
for i in stack:
    deq = deque()
    for j in i:
        if len(deq) == 0:
            deq.append(j)
        elif len(deq) > 0:
            if deq[-1] == j:
                deq.pop()
            else:
                deq.append(j)
    if len(deq) == 0:
        cnt += 1
print(cnt)


# a = list('ABBA')
# print(a)