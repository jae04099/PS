# strings = list(input())
# tenlist = ''
# for i in range(len(strings)):
#     tenlist += strings[i]
#     if len(tenlist) == 10:
#         print(tenlist)
#         tenlist = ''
# print(tenlist)

##정석
n = input()

for i in range(0, len(n), 10):
    print(n[i:i + 10])