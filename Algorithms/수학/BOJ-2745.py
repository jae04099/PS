import math

lists = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
         'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
result = 0
a, b = input().split()

for i in range(len(a)):
    result += lists.index(a[i]) * math.pow(int(b), len(a) - i - 1)
print(int(result))
