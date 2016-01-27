# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        result = self
        result.next = head
        p = result
        q = head
        while q != None:
            if q.val == val:
                p.next = q.next
            else:
                p = p.next
        
            q = q.next
        
        return result.next
