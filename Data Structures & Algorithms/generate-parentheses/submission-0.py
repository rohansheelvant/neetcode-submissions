class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def loop(string, open_no, close_no):
            if open_no == close_no == n:
                output.append(string)
            
            elif open_no == close_no:
                if open_no < n:
                    loop(string + '(', open_no+1, close_no)
            
            else:
                if open_no < n:
                    loop(string + '(', open_no+1, close_no)
                if close_no < n:
                    loop(string + ')', open_no, close_no+1)
            return 
        
        loop('', 0, 0)

        return output
            

        