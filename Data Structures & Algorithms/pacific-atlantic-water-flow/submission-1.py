class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def check_reach(row, col, name_of_set):
            name_of_set.add((row, col))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for x,y in directions:
                #print(name_of_set, row, col, row+x, col+y)
                if (row+x in range(rows) and
                    col+y in range(cols) and
                    (row+x, col+y) not in name_of_set and
                    heights[row+x][col+y] >= heights[row][col]):
                        check_reach(row+x, col+y, name_of_set)

        # Pacific
        possible_pacific = set()
        possible_atlantic = set()
        for row in range(rows):
            check_reach(row, 0, possible_pacific)
            check_reach(row, cols-1, possible_atlantic)
        for col in range(cols):
            check_reach(0, col, possible_pacific)
            check_reach(rows-1, col, possible_atlantic)
        
        #print(possible_pacific)
        #print(possible_atlantic)
        return list(possible_pacific.intersection(possible_atlantic))
        

        


                

         
        