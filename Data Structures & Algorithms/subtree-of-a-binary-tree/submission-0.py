# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isEqual(self, node1, node2):
        if node1 == node2 == None:
            return True
        elif node1 == None or node2 == None:
            return False
        elif node1.val != node2.val:
            return False
        else:
            return self.isEqual(node1.right, node2.right) and self.isEqual(node1.left, node2.left)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        bfs = [root]
        while(bfs):
            new_bfs = []
            for node in bfs:
                if node == None:
                    continue
                new_bfs.append(node.left)
                new_bfs.append(node.right)
                if self.isEqual(node, subRoot):
                    return True
            bfs = new_bfs
        
        return False
        