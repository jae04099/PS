# s = input()
# word = ''
# lists = []
# for i in range(len(s)):
#     word = s[i:len(s)]
#     lists.append(word)
# for i in range(len(lists)):
#     lists = sorted(lists, key=lambda x : (x[i]))
#     print(lists)
# for i in range(len(lists)):
#     print(lists[i])

s = input()
lists = []

for _ in s:
    lists.append(s)
    s = s[1:]
for i in sorted(lists):
    print(i)