class Solution:
    def numDecodings(self, s: str) -> int:
        possible_decode = []
        for i in range(1,27):
            possible_decode.append(str(i))
        
        return self.possibleWays(s, possible_decode)
        

    def possibleWays(self, s: str, possible_decode: list) -> int:
        if len(s) == 1 and s in possible_decode:
            return 1
        elif len(s) == 1 and s not in possible_decode:
            return 0
        elif len(s) == 0:
            return 1
        else:
            poss1 = 0
            poss2 = 0
            if s[-1] in possible_decode:
                poss1 = self.possibleWays(s[:-1], possible_decode)
            if s[-2:] in possible_decode:
                poss2 = self.possibleWays(s[:-2], possible_decode)
            
            return poss1+poss2

        