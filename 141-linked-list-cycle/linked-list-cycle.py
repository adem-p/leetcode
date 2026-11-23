# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Slow Fast Algo 
# One will go +1 other will do +2
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            fast = head.next.next
            slow = head
        except:
            return False
        
        while fast and slow:
            try:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    return True
            except:
                # No loop we went too far
                return False
        return False
