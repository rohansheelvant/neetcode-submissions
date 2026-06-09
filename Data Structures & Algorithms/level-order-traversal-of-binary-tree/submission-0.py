# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return_list = []
        bfs = [root]
        while(bfs):
            new_bfs = []
            val_list = []
            for node in bfs:
                if node == None:
                    continue
                val_list.append(node.val)
                new_bfs.append(node.left)
                new_bfs.append(node.right)
            if len(val_list) > 0:
                return_list.append(val_list)
            bfs = new_bfs
        
        return return_list
        