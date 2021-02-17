# m = input()
# n = int(m)
# lists = []

# def bunhae(x):
#     result = 0
#     for i in x:
#         result += int(i)
#     result += int(x)
#     return result

# while True:
#     if bunhae(m) == n:
#         lists.append(m)
#         m = int(m) - 1
#         m = str(m)
#     elif bunhae(m) == 0:
#         break
#     else:
#         m = int(m) - 1
#         m = str(m)

# if len(lists) == 0:
#     print(0)
# elif len(lists) > 1:
#     print(lists[len(lists) - 1])
# else:
#     print(lists[0])



# 브루트포스 문제는 단순 무식하게 접근한다.
N = int(input())
print_num = 0
for i in range(1, N+1):
    div_num = list(map(int, str(i)))
    sum_num = i + sum(div_num)
    if(sum_num == N):
        print_num = i
        break
print(print_num)