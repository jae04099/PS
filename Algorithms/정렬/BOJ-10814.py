import sys
n = int(sys.stdin.readline())
list = [list(sys.stdin.readline().split()) for _ in range(n)]

list = sorted(list, key=lambda x : int(x[0]))
for i in range(n):
    print(" ".join(list[i]))