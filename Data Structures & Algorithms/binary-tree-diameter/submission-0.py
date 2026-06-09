# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dist = 0
        def loop(node):

            nonlocal max_dist

            if node == None:
                return -1

            left_dist = loop(node.left)
            right_dist = loop(node.right)
            curr_dist = left_dist + right_dist + 2

            if curr_dist > max_dist:
                max_dist = curr_dist
            
            return max(left_dist+1, right_dist+1)
        
        loop(root)

        return max_dist




        