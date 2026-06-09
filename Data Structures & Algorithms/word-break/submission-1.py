class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        len_s = len(s)
        
        # Initialize 
        for word in wordDict:
            len_word = len(word)
            if len_word <= len_s and s[:len_word] == word:
                dp[len_word-1] = True

        for index in range(0, len(dp)):
            if dp[index] == True:
                for word in wordDict:
                    len_word = len(word)
                    if index+len_word < len_s and s[index+1:index+len_word+1] == word:
                        dp[index+len_word] = True
        
        return dp[-1]
        



        