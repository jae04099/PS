import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lists = []
for i in range(n):
    lists.append(int(input()))
start = (min(lists) * m) // n
end = max(lists) * m
while start <= end:
    
