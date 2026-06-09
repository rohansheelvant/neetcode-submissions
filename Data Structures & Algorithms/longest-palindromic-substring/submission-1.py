class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        longest_len = 1

        # Odd length palindrome
        for middle_index in range(0, len(s)):
            max_extention = min(middle_index, len(s)-middle_index-1)
            palindrome = True
            for extend in range(1, max_extention+1):
                if s[middle_index-extend] != s[middle_index+extend]:
                    palindrome = False 
                    break
                else:
                    if 2*extend+1 > longest_len:
                        longest = s[middle_index-extend:middle_index+extend+1]
                        longest_len = len(longest)

        # Even length palindrome
        for middle_index in range(0, len(s)-1):
            max_extention = min(middle_index, len(s)-middle_index-2)
            palindrome = True
            if s[middle_index] == s[middle_index+1]:
                #print("sd", middle_index, max_extention)
                for extend in range(0, max_extention+1):
                    print(middle_index, extend)
                    if s[middle_index-extend] != s[middle_index+1+extend]:
                        palindrome = False 
                        break
                    else:
                        if 2*extend+2 > longest_len:
                            longest = s[middle_index-extend:middle_index+extend+2]
                            longest_len = len(longest) 

        return longest       

