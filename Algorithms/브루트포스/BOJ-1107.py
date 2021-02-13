n = int(input())
m = int(input())
broken = list(map(int, input().split()))
purp = 100
cnt = 0
minus = 0
plus = 0

# while n == purp:
def searchNum(y):
    for i in broken:
        if y == str(i):
            return True
def startNum(x):
    while True:
        for i in range(len(str(x))):
            if searchNum(i):
                x -= 1
            else:
                minus = x
                break


print(startNum(n))