array = [-1] * 26
s = input()

for i in range(len(s)):
    if array[ord(s[i]) - 97] == -1 :
        array[ord(s[i]) - 97] = i
for i in range(26):
    print(array[i], end=' ')

    
