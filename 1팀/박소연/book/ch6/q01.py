# 유효한 펠린드롬 - 거꾸로해도 똑같은 문자열인지
# 문자열 입력 -> .isalnum() -> true면 elem.lower() 리스트에 추가 -> .reverse() -> 같은 지 비교
# .isalnum() : 문자열이 영어, 한글 혹은 숫자로 되어있으면 참 리턴, 아니면 거짓 리턴
# 질문1 : input_arr.reverse() -> 출력값: None???
# 답 : 문자열은 불변객체, reverse()는 객체 자체를 바꿈 so, 문자열을 집어넣으면 None을 반환 -> reversed(문자열)은 ok
# * input_arr[::-1]은 잘 나옴

# 문자열 조작 시 항상 슬라이싱을 우선으로 사용하는 편이 속도개선에 유리!

input_str = input()
check_arr = []

for elem in input_str:
  if elem.isalnum():
    check_arr.append(elem.lower())

if check_arr[::-1] == check_arr:
  print("true")
else:
  print("false")

#-------------------------답안코드1----------------------------
# .pop(0) -> 리스트에서 첫번째 인덱스 제거 후 출력
# .pop() -> 리스트에서 마지막 인덱스 제거 후 출력

# while len(check_arr) > 1:
#   if check_arr.pop(0) != input_str.pop():
#     return False
# return True

#-------------------------답안코드2----------------------------
# 리스트보다 데크(Deque)가 훨씬 빠름
# 리스트.pop(0) -> O(n) / 데크.popleft() -> O(1)

# strs: Deque = collections.deque()
# for char in s:
#   if char.isalnum():
#     strs.append(char.lower())
# while len(strs) > 1:
#   if strs.popleft() != strs.pop():
#     return False
# return True

#-------------------------제출코드----------------------------
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         check_arr = []

#         for elem in s:
#           if elem.isalnum():
#             check_arr.append(elem.lower())

#         if check_arr[::-1] == check_arr:
#           return True
#         else:
#           return False

