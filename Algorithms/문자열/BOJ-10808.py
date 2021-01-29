zerolist = [0] * 26
s = input()
for i in range(len(s)):
    zerolist[ord(s[i]) - 97] += 1
for i in range(26):
    print(zerolist[i], end=' ')
