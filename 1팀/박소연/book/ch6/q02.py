# 문자열 뒤집기 함수, 리턴 없이 리스트 내부 직접 조작
# 반복문 돌면서 대칭되는 인덱스 교환 -> left, right 포인터

input_arr = list(input())
left, right = 0, len(input_arr)-1
while left < right:
  input_arr[left], input_arr[right] = input_arr[right], input_arr[left]
  left += 1
  right -= 1
print(input_arr)

#-------------------------답안코드1----------------------------
# .reverse() 사용하기
# 리스트 -> .reverse() / 문자열, 리스트 -> [::-1] 슬라이싱

# s.reverse()
# s = s[::-1]

#-------------------------제출코드----------------------------
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         left, right = 0, len(s)-1
#         while left < right:
#           s[left], s[right] = s[right], s[left]
#           left += 1
#           right -= 1