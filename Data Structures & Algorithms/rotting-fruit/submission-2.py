class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        tracker = [[-1 for _ in range(COLS)] for _ in range(ROWS)]

        def bfs(queue):
            distance = 0
            while(queue):
                for _ in range(len(queue)):
                    x,y = queue.popleft()
                    tracker[x][y] = distance
                    for dirx, diry in directions:
                        x_new = x + dirx
                        y_new = y + diry
                        if( x_new >=0 and x_new < ROWS and
                        y_new >=0 and y_new < COLS and 
                        not visited[x_new][y_new] and 
                        grid[x_new][y_new] != 0):
                            queue.append((x_new,y_new))
                            visited[x_new][y_new] = True
                    
                distance += 1
        
        queue = deque([])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    visited[i][j] = True
        
        bfs(queue)

        print(tracker)
        max_dist = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    if tracker[i][j] == -1:
                        return -1
                    else:
                        max_dist = max(max_dist, tracker[i][j])
        
        return max_dist




        