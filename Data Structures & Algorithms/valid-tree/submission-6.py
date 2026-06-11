class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n-1:
            return False

        nodes = { i : [] for i in range(n)}

        for n1, n2 in edges:
            nodes[n1].append(n2)
            nodes[n2].append(n1)
        
        checked_nodes = set()

        def check_acyclic(node):
            q = deque([])
            q.append((node, None))
            while(q):
                ele, prev = q.popleft()
                if ele in checked_nodes:
                    return False
                checked_nodes.add(ele)
                neighbors = nodes[ele]
                for neigh in neighbors:
                    if neigh == prev:
                        continue
                    q.append((neigh, ele))
            
            return True
        
        for node in range(n):
            if node in checked_nodes:
                continue
            if not check_acyclic(node):
                return False
        
        return True


        
        

        
        