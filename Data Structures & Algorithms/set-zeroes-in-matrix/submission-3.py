class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows,cols = len(matrix), len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    # make row '#':
                    for i in range(cols):
                        if matrix[r][i] != 0:
                            matrix[r][i] = '#'
                    
                    # make col '#':
                    for j in range(rows):
                        if matrix[j][c] != 0:
                            matrix[j][c] = '#'
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '#':
                    matrix[r][c] = 0
        
        return

        
        
        