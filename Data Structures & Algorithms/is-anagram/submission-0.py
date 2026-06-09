class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = {}
        counts_t = {}
        for val in s:
            if val in counts_s:
                counts_s[val] += 1
            else:
                counts_s[val] = 1
        
        for val in t:
            if val in counts_t:
                counts_t[val] += 1
            else:
                counts_t[val] = 1

        return counts_s == counts_t
        