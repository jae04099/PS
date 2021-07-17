# fibo
# def fibo(n):
#     if n <= 1:
#         return n
#     return fibo(n-1) + fibo(n-2)

# print(fibo(66))

# dp
# def fibo_dp(num):
#     cache = [0 for index in range(num + 1)]
#     cache[0] = 0
#     cache[1] = 1

#     for i in range(2, num + 1):
#         cache[i] = cache[i - 1] + cache[i - 2]
#     return cache[num]

def int_sum(*args):
    sum = ''
    try:
        for n in args:
            sum +=  n
    except:
        print('error')
    return sum

int_sum('2', '3', '1')