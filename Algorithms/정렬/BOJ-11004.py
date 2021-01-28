import sys
n, k = map(int, sys.stdin.readline().split())
lists = list(map(int, sys.stdin.readline().split()))
lists.sort()
print(lists[k - 1])