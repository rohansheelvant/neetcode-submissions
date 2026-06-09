class Solution:
    def numDecodings(self, s: str) -> int:
        possible_decode = [str(i) for i in range(1, 27)]
        dp = [1] # initialize
        if s[0] in possible_decode:
            dp.append(1)
        else:
            dp.append(0)
        
        for index in range(1, len(s)):
            curr_val = 0
            if s[index] in possible_decode:
                curr_val += dp[-1]
            if s[index-1:index+1] in possible_decode:
                curr_val += dp[-2]
            dp.append(curr_val)
        
        return dp[-1]

        