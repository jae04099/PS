import sys

n = int(sys.stdin.readline())
lists = [list(sys.stdin.readline().split()) for _ in range(n)]
lists = sorted(lists, key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in lists:
    print(str(i[0]))