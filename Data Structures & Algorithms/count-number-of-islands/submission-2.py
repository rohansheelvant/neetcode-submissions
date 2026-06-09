class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        no_of_rows = len(grid)
        no_of_cols = len(grid[0])
        no_of_islands = 0
        for row in range(no_of_rows):
            for col in range(no_of_cols):
                if grid[row][col] == "1":
                    no_of_islands += 1
                    self.loop(row, col, grid, no_of_rows, no_of_cols)
        
        return no_of_islands


    def loop(self, row: int, column:int, grid: List[List[str]], no_of_rows:int, no_of_cols:int) -> None:
        grid[row][column] = "0"
        if row+1 < no_of_rows and grid[row+1][column] == "1":
            self.loop(row+1, column, grid, no_of_rows, no_of_cols)
        if row-1 >= 0. and grid[row-1][column] == "1":
            self.loop(row-1, column, grid, no_of_rows, no_of_cols)
        if column+1 < no_of_cols and grid[row][column+1] == "1":
            self.loop(row, column+1, grid, no_of_rows, no_of_cols)
        if column-1 >= 0. and grid[row][column-1] == "1":
            self.loop(row, column-1, grid, no_of_rows, no_of_cols)
        return
                        



        