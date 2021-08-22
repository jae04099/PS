# n이 홀수면 경우의수 0
# 1. 테이블 먼저 초기화
# class Stack:
#     def __init__(self):
#         self.list = list()

#     def push(self, data):
#         self.list.append(data)

#     def pop(self):
#         return self.list.pop()

# class Calculator:
#     def __init__(self):
#         self.stack = Stack()

#     def calculate(self, string):
#         lists = string.split()
#         for i in lists:
#             if i == '+':

#         return lists


# # Test code
# calc = Calculator()
# print(calc.calculate('4 6 * 2 / 2 +'))
# print(calc.calculate('2 5 + 3 * 6 - 5 *'))

# class Stack:

#     def __init__(self):
#         self.list = list()

#     def push(self, data):
#         self.list.append(data)

#     def pop(self):
#         return self.list.pop()

# class Calculator:

#     def __init__(self):
#         self.stack = Stack()

#     def calculate(self, string):
#         lists = string.split()
#         for i in lists:
#             if i == '+':
#                 y = self.stack.pop()
#                 x = self.stack.pop()
#                 self.stack.push(x + y)
#             elif i == '-':
#                 y = self.stack.pop()
#                 x = self.stack.pop()
#                 self.stack.push(x - y)
#             elif i == '*':
#                 y = self.stack.pop()
#                 x = self.stack.pop()
#                 self.stack.push(x * y)
#             elif i == '/':
#                 y = self.stack.pop()
#                 x = self.stack.pop()
#                 self.stack.push(x / y)
#             else:
#                 self.stack.push(int(i))
#         return int(self.stack.pop())


# calc = Calculator()

# print(calc.calculate('4 6 * 2 / 2 +'))

# print(calc.calculate('2 5 + 3 * 6 - 5 *'))

# hash_table = list([0 for i in range(8)])

# def get_key(data):
    # 특정 데이터에 대해 특정한 해시값을 리턴해줌
#     return hash(data)

# def hash_func(data):
#     return data % 8

# def save_data(data, value):
#     index_key = get_key(data)   # 충돌이 일어난 데이터 마다의 인덱스 키를 부여해서 자료를 찾기 위함
    # hash_address = hash_func(index_key)
    # 0으로 해시테이블을 초기화 시켰기 때문에 0이 아니라면 내부에 데이터가 있다는 뜻
    # 파이썬의 리스트를 써서 append 시키면 링크드리스트랑 비슷한 기능을 한다.
    # if hash_table[hash_address] != 0:
    #     for i in range(len(hash_table[hash_address])):
    #         if hash_table[hash_address][i][0] == index_key:
    #             hash_table[hash_address][i][1] = value
    #             return
    #     hash_table[hash_address].append([index_key, value])
    # else:
    #     hash_table[hash_address] = [[index_key, value]]
    # hash_table[hash_address] = value

# def read_data(data):
#     index_key = get_key(data)
#     hash_address = hash_func(index_key)
#     if hash_table[hash_address] != 0:
#         for i in range(len(hash_table[hash_address])):
#             if hash_table[hash_address][i][0] == index_key:
#                 return hash_table[hash_address][i][1]
#         return None
#     else:
#         return None
    # return hash_table[hash_address]

# save_data('Dd', '32432423')
# save_data('Data', '101293819')
# read_data('Dd')

# print(hash_table)

# def hash_func(key):
#     return ord(key[0]) % 10
 
# class HashTable:
#     def __init__(self):
#         self.table = [None]*10
 
#     def set(self, key, value):
#         self.table[hash_func(key)] = value
 
#     def get(self, key):
#         return self.table[hash_func(key)]
 
# class Node:
#     def __init__(self, key, data):
#         self.key = key
#         self.data = data
#         self.next = None
 
# class ChainedHashTable(HashTable):
#     def __init__(self):
#         super().__init__()

#     def set(self, key, value):
#         index_key = hash(key)
#         hash_address = hash_func(key)
#         if self.table[hash_address] != None:
#             for i in range(len(self.table[hash_address])):
#                 if self.table[hash_address][i][0] == index_key:
#                     self.table[hash_address][i][1] = value
#                     return
#             self.table[hash_address].append([index_key, value])
#         else:
#             self.table[hash_address] = [[index_key, value]]
        
#     def get(self, key):
#         index_key = hash(key)
#         hash_address = hash_func(key)
#         if self.table[hash_address] != None:
#             for i in range(len(self.table[hash_address])):
#                 if self.table[hash_address][i][0] == index_key:
#                     return self.table[hash_address][i][1]
#             return None
#         else:
#             return None
 
# # Test code
 
# ht = ChainedHashTable()
# ht.set('hello', 1)
# ht.set('hello2', 2)
# ht.set('hello3', 3)
# ht.set('hello4', 4)
 
# print(ht.get('hello'), end=' ')
# print(ht.get('hello2'), end=' ')
# print(ht.get('hello3'), end=' ')
# print(ht.get('hello4'), end=' ')
# print()
 
# ht.set('hello2', 5)
 
# print(ht.get('hello'), end=' ')
# print(ht.get('hello2'), end=' ')
# print(ht.get('hello3'), end=' ')
# print(ht.get('hello4'), end=' ')

# class Node:
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
 
# class Tree:
#     def __init__(self, root):
#         self.root = root
 
#     def preorder(self):
#         def _preorder(root):
#             if root is None:
#                 pass
#             else:
#                 print(root.data)
#                 _preorder(root.left)
#                 _preorder(root.right)
#         _preorder(self.root)
            
 
# # Test code
# root = Node(5, Node(2, Node(7, Node(4), Node(1)), Node(3)), Node(9, Node(6), Node(10)))
# tree = Tree(root)
# tree.preorder()

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
 
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
 
    def is_empty(self):
        if self.front == None:
            return True
        else:
            return False
 
    def put(self, data):
        if self.front == None:
            self.front = Node(data)
            self.rear = self.front
        else:
            node = self.front
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.rear = new
 
    def get(self):
        pass
 
    def peek(self):
        pass
 
# Test code
queue = LinkedQueue()
 
print(queue.is_empty())
for i in range(10):
    queue.put(i)
print(queue.is_empty())
 
for _ in range(11):
    print(queue.get(), end=' ')
print()
 
for i in range(20):
    queue.put(i)
print(queue.is_empty())
 
for _ in range(5):
    print(queue.peek(), end=' ')
print()
 
for _ in range(21):
    print(queue.get(), end=' ')
print()
print(queue.is_empty())