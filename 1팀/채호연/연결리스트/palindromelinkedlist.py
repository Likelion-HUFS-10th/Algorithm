# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
1. 리스트 변환 풀이. 도저히 인풋값의 형식과 이 친구가 어떤 데이터타입으로 입력되는 지 알기 어렵다.
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

2. 데크를 이용한 최적화
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: Deque = collections.deque()
        if not head: # 도대체 이 부분은 무엇을 의미하는 지 정중히 질문 드려보기.
            return True
        node = head
        
        while node is not None:
            q.append(node.val)
            node = node.next
            
            
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        
        return True
 # 데크를 이용한 투 포인터 해결방식은 반드시 이번 주 내에 복습하고 다시 숙지할 것

##개에중요한 런너를 이용한 우아한 풀이
def isPalindrome(self, head: ListNode) -> bool:
    rev = None
    slow = fast = head #같은 시작점 지정

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev
'''
#같은 원리지만 좀 더 직관적이고 이해하기 쉬운 풀이.
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        head_list = []
        while head:
            head_list.append(head.val)
            head = head.next
        return head_list == head_list[::-1]