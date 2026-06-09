# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        track = root

        while(list1 and list2):
            if list1.val >= list2.val:
                track.next = ListNode(val=list2.val)
                track = track.next
                list2 = list2.next
            else:
                track.next = ListNode(val=list1.val)
                track = track.next
                list1 = list1.next
        
        if list1:
            track.next = list1
        if list2:
            track.next = list2
        
        return root.next
        