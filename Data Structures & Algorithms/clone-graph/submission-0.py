"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hash_map = {}

        def copy_node(node):
            new_node = Node(val=node.val)
            hash_map[node] = new_node

            new_neighbors = []
            for neighbor in node.neighbors:
                if neighbor in hash_map:
                    new_neighbors.append(hash_map[neighbor])
                else:
                    new_neighbors.append(copy_node(neighbor))
            
            new_node.neighbors = new_neighbors
            return new_node
            
        if not node:
            return None
        else:
            return copy_node(node)

        
        
        