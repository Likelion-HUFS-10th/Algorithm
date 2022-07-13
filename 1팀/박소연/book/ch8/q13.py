# 팰린드롬 연결 리스트
# 거꾸로해도 똑같은지 판별
# split("->")해서 리스트로 분해 -> reverse()하고 비교

input_list = input()
split_list = input_list.split("->")
reverse_list = split_list[::-1]

if split_list == reverse_list:
  print("true")
else:
  print("false")

##########################정답코드###################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:

# def isPalindrome(self, head: ListNode) -> bool:
#   q: List = []

#   if not head:
#     return True

#   node = head
#   # 리스트 변환
#   while node is not None:
#     q.append(node.val)
#     node = node.next

#   # 팰린드롬 판별
#   while len(q) > 1:
#     if q.pop(0) != q.pop():
#       return False
#   return True