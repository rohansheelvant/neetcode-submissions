# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkBST(self, node, more_than, less_than):
        if node == None:
            return True
        elif more_than!=None and node.val <= more_than:
            return False
        elif less_than!=None and node.val >= less_than:
            return False
        else:
            return self.checkBST(node.left, more_than, node.val) and self.checkBST(node.right, node.val, less_than)


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkBST(root, None, None)



        