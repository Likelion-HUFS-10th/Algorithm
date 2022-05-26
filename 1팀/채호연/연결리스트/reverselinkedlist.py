'''
1. 재귀구조로 뒤집기

def reverselist(self, head: ListNode) -> ListNode:
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)
    
    return reverse(head)

2. 반복구조로 뒤집기
def reverseList(self, head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next
    
    return prev
'''