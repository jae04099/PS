# import sys
# input = sys.stdin.readline
# a, b = map(int, input().split())
# for i in range(a, b + 1):
#     count = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         print(i)


# def isPrime(num):
#     if num == 1:
#         return False
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num%i == 0:
#                 return False
#         return True

# M, N = map(int, input().split())

# for i in range(M, N+1):
#     if isPrime(i):
#         print(i)


def isPrime(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

m, n = map(int, input().split())
for i in range(m, n + 1):
    if isPrime(i):
        print(i)