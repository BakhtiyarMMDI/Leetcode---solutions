# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None 
        if head.next is None:
            return None
        
        count = 0
        current = head 

        while current:
            count += 1
            current = current.next
        
        middle = count // 2
        current = head
        for _ in range (middle - 1):
            current = current.next 
        current.next = current.next.next
    
        return head 

        
        