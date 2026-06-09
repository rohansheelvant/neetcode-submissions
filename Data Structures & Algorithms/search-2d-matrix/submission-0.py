class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        ll, rr = 0, (rows*cols)-1
        while(ll <= rr):
            mid = (ll+rr) // 2

            r, c =  ll//cols, ll%cols
            if matrix[r][c] == target:
                return True
            
            r, c =  rr//cols, rr%cols
            #print("right", r, c)
            if matrix[r][c] == target:
                return True
            
            r, c =  mid//cols, mid%cols
            if matrix[r][c] == target:
                return True
            
            elif target > matrix[r][c]:
                ll = mid + 1
            
            elif target < matrix[r][c]:
                rr = mid - 1
            
            #print(ll, rr, mid)
            
        return False

            
            
        