class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"],
        }
        
        output = []

        def loop(string, number):
            if len(number) == 0:
                if string:
                    output.append(string)
                return
            
            num = number[0]
            number = number[1:]

            for val in mapping[num]:
                loop(string+val, number)
            
            return
        
        loop("", digits)
    
        return output
                    