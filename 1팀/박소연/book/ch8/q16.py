# 두 수의 덧셈
# 역순으로 저장된 연결 리스트의 숫자를 더하라

class plusTwoNumber():
  def __init__(self, input_str):
    # input_str을 list로 쪼개고
    self.inputlist = input_str.split("+")
    # ['2', '4', '3'] / ['5', '6', '4'] 
    self.first = self.inputlist[0].replace("(", "").replace(") ", "").split("->")
    self.second = self.inputlist[1].replace(" (", "").replace(")", "").split("->")
  
  def plus(self):
    # 뒤집고
    reversed_first, reversed_second = self.first[::-1], self.second[::-1]
    # 문자열로 합친걸 정수형으로 형변환
    first_num, second_num = int("".join(reversed_first)), int("".join(reversed_second))
    # 더한 후 문자열로 바꾸고 리스트로 형변환
    result = list(str(first_num + second_num))
    print(" -> ".join(result[::-1]))

obj = plusTwoNumber("(2->4->3) + (5->6->4)")
obj.plus()