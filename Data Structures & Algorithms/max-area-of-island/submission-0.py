class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        m, n = len(grid[0]), len(grid)
        
        def find_area(x, y):
            if grid[y][x] == 1:
                area = 1
                grid[y][x] = '#'
            else:
                return 0

            for direction in directions:
                x_new, y_new = x+direction[0], y+direction[1]
                if x_new >= 0 and x_new < m and y_new >=0 and y_new < n:
                    if grid[y_new][x_new] == 1:
                        area += find_area(x_new, y_new)
            
            return area
        
        max_area = 0

        for x in range(0, m):
            for y in range(0, n):
                if grid[y][x] == 1:
                    current_area = find_area(x, y)
                    max_area = max(max_area, current_area)
        
        return max_area
                    
                        
