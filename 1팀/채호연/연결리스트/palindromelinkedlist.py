# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q = []
        if not head: # 도대체 이 부분은 무엇을 의미하는 지 정중히 질문 드려보기.
            return True
        node = head
        
        while node is not None:
            q.append(node.val)
            node = node.next
            
            
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        
        return True