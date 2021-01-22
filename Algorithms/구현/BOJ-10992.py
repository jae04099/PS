# n = int(input())
# line = n * 2 - 1
# star = '*'
# space = ' '
# for i in range(line, 0, -1):
#     if i == line:
#         print(space * (line // 2), end = '')
#         print(star)
#     elif i == 1:
#         print(star*line)
#     elif i % 2 == 0:
#         print(space)
#     elif i % 2 == 1:
#         print(space * ((line - (line - i + 1)) // 2) + star, end = '' )
#         print(space * (line - i - 1) + star)

n = int(input())
line = n * 2 - 1
star = '*'
space = ' '
for i in range(n, 0, -1):
    if i == n:
        print(space * (line // 2), end = '')
        print(star)
    elif i == 1:
        print(star*line)
    else:
        print(space * (i-1) + star, end = '' )
        print(space * (line - i*2) + star)
