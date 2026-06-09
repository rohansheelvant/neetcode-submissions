class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            track = set()
            for val in row:
                if val == ".":
                    continue
                if val in track:
                    return False
                else:
                    track.add(val)
        
        # check cols:
        for col in range(len(board[0])):
            track = set()
            for row in range(len(board)):
                val = board[row][col]
                if val == ".":
                    continue
                if val in track:
                    return False
                else:
                    track.add(val)
        
        # Check 3*3 boxes:
        for i in range(3):
            for j in range(3):
                track = set()
                for row in range(i*3, i*3+3):
                    for col in range(j*3, j*3+3):
                        val = board[row][col]
                        if val == ".":
                            continue
                        if val in track:
                            return False
                        else:
                            track.add(val)
        
        return True
        