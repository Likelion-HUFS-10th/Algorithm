# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a=int(len(head)/2)
        for i in range(a):
            if len(head)%2==0:
                if head[i]==head[-i-1]:
                    print('true')
                else:
                    print('false')
                    
            else:
                if head[i]==head[-i-1]:
                    print('true')
                else:
                    print('false')


TypeError: object of type 'ListNode' has no len()
    a=int(len(head)/2)
Line 8 in isPalindrome (Solution.py)
    ret = Solution().isPalindrome(param_1)
Line 40 in _driver (Solution.py)
    _driver()
Line 51 in <module> (Solution.py)