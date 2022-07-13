# 연결리스트 : 데이터 요소의 선형 집합, 데이터가 메모리에 물리적인 순서대로 저장되지X
# 동적으로 새로운 노드 삽입, 삭제 간편
# 노드 : 데이터 + 포인터 -> 포인터가 다음이나 이전 노드와의 연결 담당
# but 특정 인덱스에 접근 하려면 전체를 읽어야 함 -> so, 탐색 = O(n)
# 시작 또는 끝 지점에 삽입, 삭제, 추출은 O(1)

# 클래스 : 변수와 함수를 묶어서 하나의 새로운 객체로 만드는 것
# 클래스 자체는 객체니까 클래스를 실제로 사용하려면 인스턴스를 생성해야 함
# 인스턴스 = 붕어빵, 클래스 = 붕어빵 틀
# 인스턴스 = 클래스명() 형식
# self? 인스턴스 자기 자신

class Person:
  def __init__(self):
    self.hello = "안녕"
  def greeting(self):
    print(self.hello)
james = Person()
james.greeting()
# 1. line 18 : Person() -> Person 클래스로 가서 self에 Person()이 들어감
# 2. james의 hello 속성은 "안녕", greeting 메소드는 print(self.hello)
# 3. line 19 : james의 greeting() 메소드 실행 -> print(self.hello) -> self는 james 인스턴스 -> james의 hello 속성은 "안녕"이니까 print("안녕")

#########################################코드1##############################################

# 노드 구현
# 1. 한 개의 노드를 생성하려면 반드시 data가 매개변수로 들어와야 함 -> Node(data)
# 2. __init__ 생성자 함수: '이런 노드를 만들거다' -> 인스턴스 초기화, 가장 먼저 실행
# 3. 한 개의 노드에는 속성이 2가지 있음 -> data와 next -> 여기서 data는 데이터, next는 포인터의 역할
class Node1:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

# 연결 리스트 구현
# 1. 생성자 함수: 가장 처음 실행되는 함수 -> 첫번째 노드가 head -> head는 고정, 무조건 head를 통해서 탐색, 참조
class LinkedList1:
  def __init__(self, data):
    self.head = Node1(data) # next 매개변수를 안넘겨주면 자동으로 head가 됨
    # self.tail = None
    # self.nodecount = 0

  #헤더부터 탐색해 뒤에 새로운 노드 추가하기
  def append(self, data):
    # 새로운 노드 추가
    cur = self.head
    # 현재 노드의 next 속성 즉, 포인터가 다른 노드를 가리키고 있으면 -> 처음에는 아무것도 안 가리키고 있으니까 pass
    while cur.next is not None:
      cur = cur.next
    cur.next = Node1(data)
    print(str(cur.data) + "->")

  #모든 노드 값 출력
  def print_all(self):
    cur = self.head
    while cur is not None:
      print(cur.data, "->")
    cur = cur.next

  #노드 인덱스 알아내기
  def get_node(self, index):
    cnt = 0
    node = self.head
    while cnt < index:
      cnt += 1
      node = node.next
    return node

  #특정 인덱스 삽입
  def add_node(self, index, value):
    new_node = Node1(value)
    if index == 0:
      new_node.next = self.head
      self.head = new_node
      return
    node = self.get_node(index-1)
    next_node = node.next
    node.next = new_node
    new_node.next = next_node

  #삭제
  def delete_node(self, index):
    if index == 0:
      self.head = self.head.next
      return
    node = self.get_node(index-1)
    node.next = node.next.next


# example1.print_all()

#########################################코드2##############################################

class Node2(object):
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList2(object):
  def __init__(self):
    self.head = None
    self.count = 0

  def append(self, node):
    if self.head == None:
      self.head = node
    else:
      cur = self.head
      while cur.next != None:
        cur = cur.next
      cur.next = node
  
  def getIndex(self, data):
    curn = self.head
    idx = 0
    while curn:
      if curn.data == data:
        return idx
      curn = curn.next
      idx += 1
    return -1

  def printAll(self):
    curn = self.head
    string = ""
    while curn:
      string += str(curn.data)
      if curn.next:
        string += "->"
      curn = curn.next
    print(string)

example2 = LinkedList2()
example2.append((Node2(1)))
example2.append((Node2(2)))
example2.append((Node2(3)))
example2.printAll()