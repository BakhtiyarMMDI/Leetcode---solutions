# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        # Find beginning of second half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        current = slow

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Calculate twin sums
        first = head
        second = prev
        maximum = 0

        while second:
            maximum = max(maximum, first.val + second.val)
            first = first.next
            second = second.next

        return maximum