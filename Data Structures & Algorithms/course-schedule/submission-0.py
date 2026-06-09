class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque

        hm = {}

        for val in prerequisites:
            x,y = val[0], val[1]
            if x in hm:
                hm[x].append(y)
            else:
                hm[x] = [y]
            que = deque()
            que.append(y)
            while que:
                curr = que.popleft()
                if curr == x:
                    return False
                if curr in hm:
                    for item in hm[curr]:
                        que.append(item)
        
        return True

        