# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        number_of_nodes = 0

        def loop(node, max_val):
            nonlocal number_of_nodes
            if node == None:
                return 
            
            if node.val >= max_val:
                number_of_nodes += 1
                max_val = node.val
            
            loop(node.left, max_val)
            loop(node.right, max_val)
        
            return
        
        loop(root, -101)

        return number_of_nodes
            


        