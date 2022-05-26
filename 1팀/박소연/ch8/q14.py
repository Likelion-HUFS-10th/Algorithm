# 두 정렬 리스트의 병합
# 정렬되어 있는 두 연결 리스트 합치기
# 두 리스트 합쳐서 sort 한 후 .join("->")으로 합치기

class extendList():
  def __init__(self, input_list):
    self.inputlist = input_list
  
  def plus(self):
    split_list = self.inputlist.split(", ") # [["1->2->4"], ["1->3->4"]
    number_list = [elem.split("->") for elem in split_list] # [['1', '2', '4'], ['1', '3', '4']]
    total_list = []
    # 주의: total_list = [total_list.extend(number_list[i]) for i in range(0, len(number_list))] -> None뜸 extend는 total_list를 바꿔서 재할당할 필요X
    [total_list.extend(number_list[i]) for i in range(0, len(number_list))] # ['1', '2', '4', '1', '3', '4']
    sorted_list = sorted(total_list)
    # 구분자.join(리스트)
    print("->".join(sorted_list))

obj = extendList("1->2->4, 1->3->4")
obj.plus()
