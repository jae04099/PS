# import sys

# n = int(sys.stdin.readline())
# lists = [list(sys.stdin.readline().split()) for _ in range(n)]
# lists = sorted(lists, key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
# for i in lists:
#     print(str(i[0]))


import sys

def push(x):
    stack.append(x)

def pop():
    if (not stack):
        return -1
    else:
        return stack.pop()

def size():
    return len(stack)

def empty():
    return 0 if stack else 1

def top():
    return stack[-1] if stack else -1

n = int(sys.stdin.readline().rstrip())
stack = []

for i in range(n):
    answer = sys.stdin.readline().rstrip().split()
    order = answer[0]
    if order == "push":
        push(answer[1])
    elif order == 'pop':
        print(pop())
    elif order == 'size':
        print(size())
    elif order == 'empty':
        print(empty())
    elif order == 'top':
        print(top())
