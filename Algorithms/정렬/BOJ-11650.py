import sys
n = int(sys.stdin.readline())
list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

list = sorted(list, key=lambda x: (x[0], x[1]))
str1 = " "

for i in range(n):
    print(str1.join(map(str, list[i])))