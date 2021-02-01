# import sys

# n = int(sys.stdin.readline())
# lists = [0] * 100001
# result = 0
# mini = 0
# for i in range(n):
#     lists[int(sys.stdin.readline())] += 1
# for i in range(100001):
#     if mini < lists[i]:
#         mini = lists[i]
#         result = i
# sys.stdout.writelines(result)

# import sys
# n = int(input())
# my_dict = {}

# for i in range(n):
#     num = int(sys.stdin.readline())
#     if num not in my_dict.keys():
#         my_dict[num] = 1
#     else:
#         my_dict[num] += 1
# max_num = max(list(my_dict.values()))
# answer = []

# for key, value in my_dict.items():
#     if value == max_num:
#         answer.append(key)
# print(min(answer))

