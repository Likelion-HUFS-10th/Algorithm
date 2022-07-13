# 큐를 이용한 스택 구현
# FIFO -> LIFO
# push(x) : 요소 x를 스택에 삽입 -> 삽입하고 가장 최근에 삽입한 요소를 맨 앞으로 재정렬
# pop() : 첫 번째 요소 삭제
# top() : 첫 번째 요소 가져오기
# empty() : 스택이 비어있는지 여부 리턴

class Stack:
  def __init__(self):
    self.que = []
    # self.que = collections.deque() -> 큐를 데크로 선언
  
  def push(self, x):
    self.que.append(x)
    self.que.reverse()
    # for _ in range(len(self.que) - 1):
      # self.que.append(self.que.popleft())
      # popleft?
      # 리스트의 pop() : O(1) / pop(0) : O(n) -> 리스트의 크기에 따라 달라짐
      # 데크의 popleft() : 리스트의 pop(0)과 같은 기능이지만 시간은 O(1)
  
  def pop(self):
    return self.que.popleft()
  
  def top(self):
    return self.que[0]
  
  def empty(self):
    return len(self.que) == 0