from collections import deque
import sys
a = int(sys.stdin.readline())
queue = deque()
ans = 0

def forQueue(prop):
    if 'push' in prop:
        queue.append(int(prop[5:]))
    elif 'pop' in prop:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif 'size' in prop:
        print(len(queue))
    elif 'empty' in prop:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif 'front' in prop:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif 'back' in prop:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue) - 1])

for i in range(a):
    question = sys.stdin.readline()
    forQueue(question)

# queue = []
# prop = 'push 13243242'
# queue.append(int(prop[5:]))
# print(queue)