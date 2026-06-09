# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr_unit = None

        referenceNode = ListNode()
        track = referenceNode

        while(l1 or l2 or carry):
            l1_val = 0 if not l1 else l1.val
            l2_val = 0 if not l2 else l2.val

            curr_unit = l1_val + l2_val + carry
            carry = 0
            if curr_unit > 9:
                carry = 1
                curr_unit = curr_unit - 10
            
            track.next = ListNode(curr_unit)

            track = track.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return referenceNode.next
        