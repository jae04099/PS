n = int(input())
lists = list(range(1, n + 1))
samp = []
math = []

for i in range(n):
    samp.append(int(input()))
samp = samp.reverse()
print(samp)