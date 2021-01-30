s = input()
result = ''

for i in s:
    if i.isupper():
        if ord(i) + 13 > 90:
            result += chr(ord(i) + 13 - 90 + 64)
        elif ord(i) + 13 < 91:
            result += chr(ord(i) + 13)
    elif i.islower():
        if ord(i) + 13 > 122:
            result += chr(ord(i) + 13 - 122 + 96)
        elif ord(i) + 13 < 123:
            result += chr(ord(i) + 13)
    else:
        result += i
print(result)