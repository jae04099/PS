import sys
n = int(sys.stdin.readline())
list = list(int(sys.stdin.readline()) for _ in range(n))
list = sorted(list)

for i in list:
    print(i)