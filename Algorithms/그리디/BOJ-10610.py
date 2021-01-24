# n = input()
# numlist = []
# for i in range(len(n)):
#     numlist.append(int(n[i]))
# numlist = sorted(numlist)[::-1]
# strings = [str(numlis) for numlis in numlist]
# a_string = "".join(strings)
# an_integer = int(a_string)

# if an_integer % 30 == 0:
#     print(an_integer)
# else :
#     print(-1)


n = input()
n = sorted(n, reverse=True)
sum = 0
if '0' not in n:
    print(-1)
else:
    for i in n:
        sum += int(i)
    if sum % 3 != 0 :
        print(-1)
    else :
        print(''.join(n))