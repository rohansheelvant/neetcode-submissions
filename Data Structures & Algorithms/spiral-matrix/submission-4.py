class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 1:
            return matrix[0]

        output = []

        rows,cols = len(matrix), len(matrix[0])

        r,c = 0,0
        dr,dc = 0,1

        print(rows, cols)

        while(matrix[r][c] != "#"):
            #print(r,c, dr, dc)
            if(
                r+dr not in range(rows) or
                c+dc not in range(cols) or
                matrix[r+dr][c+dc] == "#"
            ):
                #print("R", r+dr not in range(rows), c+dc not in range(cols))

                if dr == 0 and dc == 1:
                    dr = 1
                    dc = 0
                elif dr == 1 and dc == 0:
                    dr = 0
                    dc = -1
                elif dr == 0 and dc == -1:
                    dr = -1
                    dc = 0
                elif dr == -1 and dc == 0:
                    dr = 0
                    dc = 1
                
                #print("A", r, c, dr, dc)
                output.append(matrix[r][c])
                matrix[r][c] = "#"
                r += dr
                c += dc


                if matrix[r][c] == "#":
                    break
        
            else:
                output.append(matrix[r][c])
                matrix[r][c] = "#"
                r += dr
                c += dc
        
        return output




        
        