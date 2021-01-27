import sys
n = int(sys.stdin.readline())
list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
list = sorted(list, key=lambda x : (x[1], x[0]))
for i in range(n):
    print(" ".join(map(str, list[i])))