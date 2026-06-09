# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        bfs = [root]
        depth = -1
        while(bfs):
            depth += 1
            new_bfs = []
            for node in bfs:
                if node == None:
                    continue
                new_bfs.append(node.left)
                new_bfs.append(node.right)
            bfs = new_bfs
        return depth
        