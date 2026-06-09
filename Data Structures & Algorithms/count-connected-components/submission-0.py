class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edge_hm = { i:[] for i in range(n) }

        for edge1, edge2 in edges:
            edge_hm[edge1].append(edge2)
            edge_hm[edge2].append(edge1)
        
        visited_node = set()
        total_cc = 0

        def dfs(node, parent):
            if node in visited_node:
                return
            visited_node.add(node)
            for j in edge_hm[node]:
                if j != parent:
                    dfs(j, node)
            
            return
            


        for i in range(n):
            if i not in visited_node:
                total_cc += 1
                dfs(i, -1)
        
        return total_cc

        