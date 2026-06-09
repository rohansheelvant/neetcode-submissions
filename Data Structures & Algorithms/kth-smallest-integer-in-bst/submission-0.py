# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def addNodes(self, root, stack):
        node = root
        while(node):
            stack.append(node)
            node = node.left
        return stack

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = self.addNodes(root, [])
        while(k!=0):
            last_node = stack[-1]
            stack.pop(-1)
            k -= 1
            val = last_node.val
            stack = self.addNodes(last_node.right, stack)
        
        return val



        