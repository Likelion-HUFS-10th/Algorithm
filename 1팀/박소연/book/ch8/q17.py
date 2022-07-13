# 페어의 노드 스왑
# 연결리스트를 입력받아 페어 단위로 스왑하라
# 연결리스트로 풀어보기

# class Node():
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# class nodePair():
#   def __init__(self):
#     self.head = None

#   def append(self, node):
#     if self.head == None:
#       self.head = node
#     else:
#       cur = self.head
#       while cur.next != None:
#         cur = cur.next
#       cur.next = node

#   def swap(self):
#     cur = self.head
#     while cur and cur.next:
#       cur.data, cur.next = cur.next, cur.data
#     cur = cur.next.next
#     print(self.head)

# obj = nodePair()
# obj.append(Node(1))
# obj.append(Node(2))
# obj.append(Node(3))
# obj.append(Node(4))
# obj.swap()