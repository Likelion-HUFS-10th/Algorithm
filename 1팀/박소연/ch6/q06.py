# 가장 긴 팰린드롬 부분 문자열
# 중앙을 중심으로 두 포인터 확장

def longestPalindrome(): # babad
  strs = "babad"
  def expand(left, right):
    while left >= 0 and right < len(strs) and strs[left] == strs[right]: # 
      left -= 1
      right += 1
    return strs[left+1:right]

  if len(strs) < 2 or strs == strs[::-1]: # 문자열 길이가 0 또는 1이면 뒤집어도 똑같으니까 바로 리턴
    return strs
  result = ""
  for i in range(len(strs)-1):
    result = max(result, expand(i, i+1), expand(i, i+2), key=len) 
    # expand(i, i+1) 호출 -> 결과값 리턴 -> expand(i, i+2) 호출 -> 결과값 리턴
  return result

longestPalindrome()

#-------------------------정답코드----------------------------
# class Solution:
#   def longestPalindrome(self, s: str) -> str: # babad
#     def expand(left: int, right: int) -> str:
#       while left >= 0 and right < len(s) and s[left] == s[right]: # 
#         left -= 1
#         right += 1
#       return s[left+1:right]

#     if len(s) < 2 or s == s[::-1]: # 문자열 길이가 0 또는 1이면 뒤집어도 똑같으니까 바로 리턴
#       return s
#     result = ""
#     for i in range(len(s)-1): # 문자열 인덱스 0부터 끝까지의 개수만큼 반복
#       result = max(result, expand(i, i+1), expand(i, i+2), key=len) 
#     return result