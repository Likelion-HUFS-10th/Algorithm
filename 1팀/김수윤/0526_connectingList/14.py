# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        List=list1+list2
        list3= List.sort()
        print(list3)
        
        
TypeError: unsupported operand type(s) for +: 'ListNode' and 'ListNode'
    List=list1+list2
Line 8 in mergeTwoLists (Solution.py)
    ret = Solution().mergeTwoLists(param_1, param_2)
Line 34 in _driver (Solution.py)
    _driver()
Line 45 in <module> (Solution.py)



#정답
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.cal > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1