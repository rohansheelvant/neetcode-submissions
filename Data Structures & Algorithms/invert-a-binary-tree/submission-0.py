# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        bfs = [root]
        while(bfs):
            new_bfs = []
            for node in bfs:
                if node == None:
                    continue
                node.left, node.right = node.right, node.left
                new_bfs.append(node.right)
                new_bfs.append(node.left)
            bfs = new_bfs
        
        return root
            

        