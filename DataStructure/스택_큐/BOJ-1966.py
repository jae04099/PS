# test_cases = int(input())
# for _ in range(test_cases):
#     n, m = list(map(int, input().split()))
#     imp = list(map(int, input().split()))
#     idx = list(range(len(imp)))
#     idx[m] = 'target'

#     order = 0

#     while True:
#         if imp[0] == max(imp):
#             order += 1
#             if idx[0] == 'target':
#                 print(order)
#                 break
#             else:
#                 imp.pop(0)
#                 idx.pop(0)
#         else:
#             imp.append(imp.pop(0))
#             idx.append(idx.pop(0))


test_cnt = int(input())

for i in range(test_cnt):
    n, m = map(int, input().split())
    imp = map(int, input().split())
    idx = list(int(range(len(imp))))
    idx[m] = 'target'

    order = 0

    while True:
        if imp[0] == max(imp):
            order += 1
            if idx[0] == 'target':
                print(order)
                break
            else:
                imp.pop(0)
                idx.pop(0)
        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))