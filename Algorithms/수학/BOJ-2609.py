# import sys 
# a, b = map(int, sys.stdin.readline().split())

# def gcm(x, y):   # 최대공약수
#     while y:
#         x, y = y, x % y
#     return x
# def lcm(x, y):  # 최소공배수
#     result = (x * y) // gcm(x, y)
#     return result

# print(gcm(a, b))
# print(lcm(a, b))


a, b = map(int, input().split())

def gcm(x, y):
    while y:
        x, y = y, (x % y)
    return x

def lcm(x, y):
    result = (x * y) // gcm(x, y)
    return result

print(gcm(a, b))
print(lcm(a, b))