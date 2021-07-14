# 노드 구현
# 왜 클래스를 이용하냐? 노드는 데이터와 주소값이라는 두개가 연결된 구조로 이루어져 있기 때문에, 그 구조를 만들기 위해 클래스를 쓴다.

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 노드 두 개를 만듦
node1 = Node(1)
node2 = Node(2)

# next는 다음 노드를 가리키는 주소값. 다음 노드인 node2를 가리키게 한다.
node1.next = node2
head = node1

#---------------------------------------------------

# 링크드 리스트로 데이터 추가
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def add(data):
        node = head
        while node.next:    # 다음 노드를 가리키는 주소값이 비어있다는 것은 해당 노드가 마지막 노드라는 뜻.
            node = node.next
        # 현재 노드가 끝난 후 뒤에 새로운 데이터 추가
        node.next = Node(data)

node1 = Node('first')
head = node1
Node.add('third')

# 링크드 리스트 데이터 출력하기
node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)

#--------------------------------------------------------
# 중간에 새 노드 삽입

node = head
search = True
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next
node_next = node.next
node.next = node3
node3.next = node_next


#----------------------------------------------------------
# 찐으로 구현
# 노드 하나를 만드는 클래스
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 노드의 링크드 리스트들 관리하는 클래스
class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
    # 링크드 리스트 맨 마지막에 노드 추가
    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
    # 링크드 리스트 전체 출력
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

linkedlist1 = NodeMgmt(0)

for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc()