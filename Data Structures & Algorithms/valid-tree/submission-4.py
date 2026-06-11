class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n-1:
            return False

        nodes = { i : [] for i in range(n)}

        for n1, n2 in edges:
            nodes[n1].append(n2)
            nodes[n2].append(n1)

        def check_acyclic(node):
            print(node, '=====')
            q = deque([])
            visited = set()
            q.append((node, None))
            while(q):
                ele, prev = q.popleft()
                print(ele, prev)
                if ele in visited:
                    return False
                visited.add(ele)
                neighbors = nodes[ele]
                for neigh in neighbors:
                    if neigh == prev:
                        continue
                    q.append((neigh, ele))
            
            return True
        
        for node in range(n):
            if not check_acyclic(node):
                return False
        
        return True


        
        

        
        