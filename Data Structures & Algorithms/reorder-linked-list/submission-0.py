# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        
        temp = slow.next
        slow.next = None
        slow = temp
        # reverse starting from slow index
        prev = None
        while(slow):
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # Take one from head, one from slow till end
        root = ListNode()
        track = root
        while(head and prev):
            root.next = head
            head = head.next
            root = root.next
            root.next = prev
            prev = prev.next
            root = root.next
        
        if head:
            root.next = head
        if prev:
            root.next = prev
        
        return

        