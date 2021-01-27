n = int(input())
list = []
mult = 0
plus = []
minus = []

for i in range(n):
    list.append(int(input()))

list = sorted(list)

for i in range(n):
    if list[i] <= 0:
        minus.append(list[i])
    else:
        plus.append(list[i])
if len(plus) > 1:
    mult += plus[len(plus) - 1] * plus[len(plus) - 2] + sum(minus) + sum(plus[:len(plus) - 2])
elif len(plus) == 1:
    mult += plus[0] + sum(minus)
elif len(plus) == 0 and minus[len(minus) - 1] == 0:
    if len(minus) == 1:
        mult = 0
    elif len(minus) == 2:
        mult += minus[0]
    elif len(minus) == 3:
        mult += minus[len(minus) - 2] * minus[len(minus) - 3]
    elif len(minus) > 3:
        mult += minus[len(minus) - 2] * minus[len(minus) - 3]+ sum(minus[:len(minus) - 2])



print(mult)

# if len(minus) > 1:
#         mult += minus[len(minus) - 1] * minus[len(minus) - 2] + sum(minus[:len(minus) - 3])