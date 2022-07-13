# 그룹 애너그램 -> 문자열 배열을 애너그램 단위로 그룹핑
# 애너그램 문자를 재배열해서 다른 뜻을 가진 단어로 바꾸는 것 ex) eat -> ate, tea
# 초기할당 : 문자열 정렬 리스트 -> 정렬 리스트에서 중복 제거한 길이만큼 이중리스트 생성
# 맨 처음 값을 group에 넣음 -> 그 값하고 같은 값 group에 추가 -> group에 있는 값 input에서 제거

# 1. sorted
# 1) sorted(리스트 또는 문자열)
# 2) 리스트 형태로 리턴
# 3) 문자열 형태로 다시 결합하려면 "".join(sorted(b))

def groupAnagrams():
  input_arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
  sorted_arr = [ sorted(elem) for elem in input_arr ]
  group_len = list(set([tuple(set(elem)) for elem in sorted_arr]))
  group_arr = [[] for _ in range(len(group_len))]
  i = 0

  while len(input_arr) > 0:
    group_arr[i].append(input_arr[0])
    for j in range(1, len(input_arr)):
      if sorted_arr[i] == sorted_arr[j]:
        group_arr[i].append(input_arr[j])
    input_arr = [ elem for elem in input_arr if elem not in group_arr[i]]
    i += 1
  print(group_arr)

groupAnagrams()

#-------------------------정답코드----------------------------
# class Solution:
#   def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#     anagrams = collections.defaultdic(list) # 존재하지 않는 키를 삽입할 경우 나는 에러 방지 -> 항상 디폴트 값 생성

#     for word in strs:
#       anagrams["".join(sorted(word))].append(word)
# 1) sorted(word) : strs 요소 정렬 후 리스트 리턴 -> 이중리스트 구조가 됨 
# 2) "".join() : 리스트 문자열로 합침
# 3) anagrams[] : 안에 문자열을 키로 갖는 딕셔너리 구성
# 4) .append(word) : 같은 애너그램 append
#     return list(anagrams.values())

#-------------------------제출코드----------------------------
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#       sorted_arr = [ sorted(elem) for elem in strs ]
#       group_len = list(set([tuple(set(elem)) for elem in sorted_arr]))
#       group_arr = [[] for _ in range(len(group_len))]
#       i = 0

#       while len(strs) > 0:
#         group_arr[i].append(strs[0])
#         for j in range(1, len(strs)):
#           if sorted_arr[i] == sorted_arr[j]:
#             group_arr[i].append(strs[j])
#         strs = [ elem for elem in strs if elem not in group_arr[i]]
#         i += 1