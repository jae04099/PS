import sys
n = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))
list = sorted(list)
result = 0

for i in range(n):
    result += list[i]*(n - i)
print(result)