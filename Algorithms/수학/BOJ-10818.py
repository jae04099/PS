import sys

n = int(sys.stdin.readline())
lists = list(map(int, sys.stdin.readline().split()))
setted = sorted(lists)
print('{0} {1}'.format(setted[0], setted[n-1]))