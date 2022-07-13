# 스택을 이용한 큐 구현
# LIFO -> FIFO
# push(x) : 요소 x를 큐 마지막에 삽입
# pop() : 큐 처음에 있는 요소 제거
# peek() : 큐 처음에 있는 요소 조회
# empty() : 큐가 비어 있는지 여부 리턴

class Queue:
  def __init__(self):
    self.stack = []
    # self.input = []
    # self.output = []
  
  def push(self, x):
    self.stack.append(x)
    # self.input.append(x)
  
  def pop(self):
    return self.stack.pop(0)
    # self.peek()
    # return self.output.pop()
  
  def peek(self):
    return self.stack[0]
    # if not self.output:
    #   while self.input:
    # self.output에는 input에 있는게 뒤집어져서 들어감
    #     self.output.append(self.input.pop())
    # self.output의 가장 마지막 값 = self.input의 가장 처음 값
    # return self.output[-1]
  
  def empty(self):
    return len(self.stack) == 0
    # return self.input == [] and self.output == []