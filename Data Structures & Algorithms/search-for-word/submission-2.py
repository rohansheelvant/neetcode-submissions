class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board[0]), len(board)

        def find(word: str, current: tuple, visited: List[tuple]):
            if len(word) == 1:
                x,y = current
                return board[y][x] == word[0]
            
            print(current, visited)

            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            x,y = current
            possible = False
            for x_dir, y_dir in directions:
                x_new, y_new = x+x_dir, y+y_dir

                if(board[y][x] == word[0] and
                x_new in range(rows) and
                y_new in range(cols) and 
                (x_new, y_new) not in visited):
                    visited.append((x,y))
                    possible = possible or find(word[1:], (x_new, y_new), visited)
                    visited.pop(-1)
            
            return possible

        for i in range(rows):
            for j in range(cols):
                if find(word, (i,j), [()]):
                    return True
        
        return False
        
        

