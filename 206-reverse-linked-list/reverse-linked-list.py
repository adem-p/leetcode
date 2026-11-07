# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:\

        old = None
        curr = head

        while curr != None:
            tempNext = curr.next
            curr.next = old
            old = curr
            curr = tempNext
             
        return old



        