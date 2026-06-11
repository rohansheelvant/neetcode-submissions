class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inbound = [0] * numCourses
        outbound = { i:[] for i in range(numCourses) }

        for dst, src in prerequisites:
            inbound[dst] += 1
            outbound[src].append(dst)
        
        q = deque()
        for course in range(numCourses):
            if inbound[course] == 0:
                q.append(course)
        
        courses = []
        while(q):
            ele = q.popleft()
            courses.append(ele)
            for nxt in outbound[ele]:
                inbound[nxt] -= 1
                if inbound[nxt] == 0:
                    q.append(nxt)
    
        if len(courses) == numCourses:
            return courses
        return []

        