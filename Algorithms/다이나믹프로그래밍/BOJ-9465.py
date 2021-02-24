n = int(input())
res = 0

for i in range(n):
    t = int(input())
    d = [list(map(int, input().split())) for _ in range(2)]
    for i in range(t):
        