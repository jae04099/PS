import sys
k, n = map(int,sys.stdin.readline().split())
lines = []
for i in range(k):
    lines.append(int(input()))
start = 1
end = max(lines)

while start <= end:
    middle = (end + start) // 2
    line = 0
    for i in lines:
        line += i // middle
    if line >= n:
        start = middle + 1
    else:
        end = middle - 1
print(end)