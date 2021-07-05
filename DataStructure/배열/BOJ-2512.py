import sys
n = int(sys.stdin.readline())
lists = list(map(int, sys.stdin.readline().split()))
maxMoney = int(sys.stdin.readline())
start = 0
end = max(lists)
while start <= end:
    mid = (start + end) // 2
    finMoney = 0
    for i in lists:
        if i >= mid:
            finMoney += mid
        else:
            finMoney += i
    if finMoney <= maxMoney:
        start = mid + 1
    else:
        end = mid - 1
print(end)
