# 역순 연결 리스트
# 연결 리스트를 뒤집어라
# tail 빼놓고 input_list에서 마지막 요소 pop -> input_list 뒤집어서 reversed_list에 저장 -> reversed_list에 tail 삽입 

class reverseList():
  def __init__(self, input_str):
    self.inputstr = input_str
  
  def reverse(self):
    input_list = self.inputstr.split("->") #["1", "2", "3", "4", "5", "NULL"]
    node_tail = input_list[-1]
    input_list.pop()
    reversed_list = input_list[::-1]
    reversed_list.append(node_tail)
    print("->".join(reversed_list))

obj = reverseList("1->2->3->4->5->NULL")
obj.reverse()