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
        
        while hm != {}: 
            key = list(hm.keys())[0]
            que = deque()
            check_list = set()
            check_list.add(key)
            for val in hm[key]:
                que.append(val)
            del hm[key]

            while que:
                curr = que.popleft()
                if curr in check_list:
                    return False
                if curr in hm:
                    for item in hm[curr]:
                        if item not in que:
                            que.append(item)
                    check_list.add(curr)
                    del hm[curr]
        
        return True

        