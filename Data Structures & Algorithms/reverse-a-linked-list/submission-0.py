# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currNode = head
        nextNode, new_nextNode = ListNode(val=None), None
        while(nextNode != None and currNode!=None):
            nextNode = currNode.next
            currNode.next = new_nextNode
            new_nextNode = currNode
            currNode = nextNode
        return new_nextNode
        