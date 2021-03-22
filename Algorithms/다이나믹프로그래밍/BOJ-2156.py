n = int(input())
<<<<<<< HEAD
w = [0]
for i in range(n):
    w.append(int(input()))
dp = [0]
dp.append(w[1])
=======
d = [0]*10001
lists = []
for i in range(n):
    lists.append(int(input()))
d[0] = lists[0]
d[1] = lists[1]
d[2] = lists[2]
for i in range(3, n):
    d[i] = max(d[i - 1] + d[i - 3], d[i - 2] + d[i - 3]) + d[i]
print(d)
>>>>>>> 6c0d720a0153254b47fff041b0b779440859f227
