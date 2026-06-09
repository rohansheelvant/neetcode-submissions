# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def loop(node):
            nonlocal balanced

            if node == None:
                return 0
            
            left_node = loop(node.left)
            right_node = loop(node.right)

            diff = abs(left_node - right_node)
            if diff > 1:
                balanced = False
            
            return max(left_node, right_node) + 1
        
        loop(root)

        return balanced

        