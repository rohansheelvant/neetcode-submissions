# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        output = []

        def loop(node, level):
            nonlocal output
            if node == None:
                return
            # level starts with 0
            if len(output) <= level:
                output.append(node.val)
            
            loop(node.right, level + 1)
            loop(node.left, level + 1)
        
            return
        
        loop(root, 0)

        return output
        