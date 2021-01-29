import sys

n = int(sys.stdin.readline())
lists = [0] * 100001
result = 0
mini = 0
for i in range(n):
    lists[int(sys.stdin.readline())] += 1
for i in range(100001):
    if mini < lists[i]:
        mini = lists[i]
        result = i
sys.stdout.writelines(result)