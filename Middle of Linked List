"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    # @param head: the head of linked list.
    # @return: a middle node of the linked list
    def middleNode(self, head):
        # Write your code here
        if head==None or head.next==None:
            return head
        else:
            single = head
            double = head.next
            while double !=None and double.next != None:
                
                single = single.next
                double = double.next.next
        
        return single
            
