class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix)
        if rows == 1:
            return matrix
        
        iters = rows // 2
        for i in range(iters):
            curr_r = i
            for col in range(i, cols-i-1):
                curr_c = col
                temp = matrix[curr_r][curr_c]

                # 1st time
                future_r, future_c = curr_c, cols-curr_r-1
                #print(f"1 - ({curr_r},{curr_c}), ({future_r},{future_c}), {temp}")
                temp, matrix[future_r][future_c] = matrix[future_r][future_c], temp
                curr_r, curr_c = future_r, future_c

                # 2nd time
                future_r, future_c = curr_c,cols-1-curr_r
                #print(f"2 - ({curr_r},{curr_c}), ({future_r},{future_c}), {temp}")
                temp, matrix[future_r][future_c] = matrix[future_r][future_c], temp
                curr_r, curr_c = future_r, future_c

                #3rd time
                future_r, future_c = curr_c, rows-1-curr_r
                #print(f"3 - ({curr_r},{curr_c}), ({future_r},{future_c}), {temp}")
                temp, matrix[future_r][future_c] = matrix[future_r][future_c], temp
                curr_r, curr_c = future_r, future_c

                #4th time
                future_r, future_c = curr_c, cols-1-curr_r
                #print(f"4 - ({curr_r},{curr_c}), ({future_r},{future_c}), {temp}")
                temp, matrix[future_r][future_c] = matrix[future_r][future_c], temp
                curr_r, curr_c = future_r, future_c
        
        return
        