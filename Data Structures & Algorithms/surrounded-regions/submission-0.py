import copy

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(x,y):
            "Returns if the current region should be converted to X"
            q = deque([(x,y)])
            visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
            visited[x][y] = True

            region_cells = [(x, y)]
            enclosed = True
            while(q):
                a, b = q.popleft()
                if board[a][b] == "O":
                    if(a in [0, ROWS-1] or b in [0, COLS-1]):
                        enclosed = False
                    for dirx, diry in directions:
                        a_new = a + dirx
                        b_new = b + diry
                        if( a_new >= 0 and a_new < ROWS and
                        b_new >= 0 and b_new < COLS and
                        not visited[a_new][b_new] and
                        board[a_new][b_new] == "O"):
                            q.append((a_new, b_new))
                            visited[a_new][b_new] = True
                            region_cells.append((a_new, b_new))
            
            if enclosed:
                for r, c in region_cells:
                    board[r][c] = "X"
            return

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    bfs(i,j)
        