"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        referenceNode = Node(0)
        track = {}
        headcopy = head

        currNode = referenceNode
        while(head):
            newNode = Node(head.val)
            currNode.next = newNode
            track[head] = newNode
            currNode = currNode.next
            head = head.next
        
        while(headcopy):
            currNode = track[headcopy]
            if headcopy.random:
                currNode.random = track[headcopy.random]
            headcopy = headcopy.next
        
        return referenceNode.next

