#1. Node 정의
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

#2. Node 생성해보기
node1 = Node(1) 

#3. Node의 값, 포인터 출력하기
print(node1.data)
print(node1.next)

#4. 노드끼리 연결하기
node2 = Node(3)
node1.next = node2 
'''바로 이 16행이 가장 중요. '='을 통해 값 자체를 그대로 node1.next로 넣어주는 게 아니라 node2를 참조하도록 '연결' 지시를 한 거라는 것!
   바로 여기서 두 노드가 연결되는 magic!.
   이걸 어떻게 아냐고?
   후에 == 가 아닌 is 비교를 통해 두 객체가 완전하게 동일(identical same)인지 확인할 예정.
'''
head = node1 #뭐야 진짜 수동으로 정해주는 거네;
print(node1.next is node2) # is를 통해 확인해보면 node1.next와 node2가 참조하는 값의 주소가 아예 일치하는 것을 확인 할 수 있다.
print(node1.next.data)
print(node2.data)
print(node2.next)

#5. 노드 뒤에 값(tail)추가하는 법
def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

node1 = Node(1)
head = node1
add(3)
print(node1)
print(node1.next.data)

