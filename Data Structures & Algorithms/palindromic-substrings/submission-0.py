class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0

        # Odd length palindrome
        for middle_index in range(0, len(s)):
            max_extention = min(middle_index, len(s)-middle_index-1)
            palindrome = True
            for extend in range(0, max_extention+1):
                if s[middle_index-extend] != s[middle_index+extend]:
                    palindrome = False 
                    break
                else:
                    total += 1

        # Even length palindrome
        for middle_index in range(0, len(s)-1):
            max_extention = min(middle_index, len(s)-middle_index-2)
            palindrome = True
            if s[middle_index] == s[middle_index+1]:
                for extend in range(0, max_extention+1):
                    print(middle_index, extend)
                    if s[middle_index-extend] != s[middle_index+1+extend]:
                        palindrome = False 
                        break
                    else:
                        total += 1 

        return total       

