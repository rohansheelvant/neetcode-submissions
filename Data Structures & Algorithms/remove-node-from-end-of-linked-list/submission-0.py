# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total_len = 0
        track = head
        while(track):
            total_len += 1
            track = track.next
        
        node_to_remove = total_len + 1 - n

        track = head
        curr_len = 0
        prev = ListNode(next=track)
        return_node = prev
        while(track):
            curr_len += 1
            if curr_len == node_to_remove:
                track = track.next
                prev.next = track
                continue
            
            prev = track
            track = track.next

        return return_node.next
        