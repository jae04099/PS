n = int(input())
def lcm(x, y):
    result = (x * y) // gcm(x, y)
    return result
def gcm(x, y):
    while y:
        x, y = y, (x % y)
    return x

for i in range(n):
    a, b = map(int, input().split())
    print(lcm(a, b))