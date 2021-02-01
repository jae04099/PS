n = int(input())
for i in range(n):
    str = input().rstrip()
    left, right = 0, 0

    for i in range(len(str)):
        if str[i] == '(':
            left += 1
        elif str[i] == ')':
            right += 1
        if right > left:
            print('NO')
            break
    if left == right:
        print('YES')
    elif right < left:
        print('NO')

