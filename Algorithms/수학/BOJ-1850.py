import sys
a, b = map(int, sys.stdin.readline().split())

def gcm(x, y):
    while y:
        x, y = y, (x % y)
    return x
result = gcm(a, b) * '1'
sys.stdout.writelines(result)