# 역순 연결 리스트2
# 인덱스 m에서 n까지를 역순으로 만들어라

class reverseList2():
  def __init__(self, input_str, m, n):
    self.inputstr = input_str
    self.m = m
    self.n = n
  
  def reverse(self):
    # input 문자열 화살표 기준으로 쪼개고
    input_list = self.inputstr.split("->")
    # 첫번째 그룹 = 0 ~ self.m
    first_list = [input_list[i] for i in range(0, self.m-1)]
    # 두번째 그룹 = self.m ~ self.n -> 뒤집기
    second_list = [input_list[i] for i in range(self.m-1, self.n)][::-1]
    # 세번째 그룹 = self.n ~ 끝
    third_list = [input_list[i] for i in range(self.n-1, len(input_list))]
    reversed_list = first_list + second_list + third_list
    print("->".join(reversed_list))

obj = reverseList2("1->2->3->4->5->NULL", 2, 4)
obj.reverse()