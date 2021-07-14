lists = list(input())
sum = 0
stack = []

for i in range(len(lists)):
    if lists[i] == '(':
        stack.append(lists[i])
    else:
        if lists[i - 1] == '(':
            stack.pop()
            sum += len(stack)
        else:
            stack.pop()
            sum += 1
print(sum)